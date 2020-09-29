import math
import os
from pprint import pprint

from WeatherMaker import WeatherMaker
import cv2


class ImageMaker:
    COLOR_WHITE = [255, 255, 255]
    COLOR_BLACK = [0, 0, 0]

    def __init__(self, day, matrix_weather):
        self.path_card_main = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\probe.jpg")

        self.path_card_cloud = os.getcwd() + os.path.normpath(
            "\\python_snippets\\external_data\\weather_img\\cloud.jpg")
        self.path_card_rain = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\weather_img\\rain.jpg")
        self.path_card_snow = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\weather_img\\snow.jpg")
        self.path_card_sun = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\weather_img\\sun.jpg")

        self.main_card = None
        self.height_main_card = None
        self.width_main_card = None
        self.size_main_card = None

        self.weather_card = None
        self.width_weather_card = None
        self.height_weather_card = None
        self.size_weather_card = None

        self.matrix_weather = matrix_weather
        self.day = day

    def run(self):
        self.create_main_card()
        self.creating_card_for_specific_day()

    def creating_card_for_specific_day(self):
        COLOUR_BLUE = [255, 255, 0]
        COLOUR_YELLOW = [0, 255, 255]
        COLOUR_DARK_BLUE = [255, 0, 0]
        COLOUR_GRAY = [127, 127, 127]

        if self.matrix_weather[self.day]["погода"] in ['Ясно', 'Солнечно', 'Ясная погода', 'Малооблачно']:
            self.painting_picture(colour=COLOUR_YELLOW, smiley_path=self.path_card_sun)
        elif self.matrix_weather[self.day]["погода"] in ['Дождь']:
            self.painting_picture(colour=COLOUR_DARK_BLUE, smiley_path=self.path_card_rain)
        elif self.matrix_weather[self.day]["погода"] in ['Снег']:
            self.painting_picture(colour=COLOUR_BLUE, smiley_path=self.path_card_snow)
        elif self.matrix_weather[self.day]["погода"] in ['Облачно', "Пасмурно"]:
            self.painting_picture(colour=COLOUR_GRAY, smiley_path=self.path_card_cloud)
        else:
            print("Необходимо добавить такой тип погоды :", self.matrix_weather[self.day]["погода"])
            self.painting_picture(colour=COLOUR_GRAY, smiley_path=self.path_card_cloud)

        self.save_card()

    def save_card(self):
        filedir = "weather_pictures"
        if not os.path.exists(filedir):
            os.mkdir(filedir)
        filename = str(self.day)+'.jpg'
        path = os.path.join(filedir, filename)
        path = os.path.normpath(path)
        cv2.imwrite(path, self.main_card)


    def painting_picture(self, colour, smiley_path):
        self.weather_picture(smiley_path)
        self.background_coloring(colour=colour)
        self.gluing()
        self.add_text()
        self.schow_card(self.main_card, "main")

    def add_text(self):

        date = self.day
        weather = self.matrix_weather[self.day]["погода"]
        temper = self.matrix_weather[self.day]["температура"].replace('…', '...')[:-1]
        Y = self.height_main_card // 2
        (x_down_left, y_down_left) = (self.width_main_card // 3, Y)
        size_text = 1
        color = (111, 111, 190)
        size_letters = 3

        cv2.putText(self.main_card, date, (x_down_left, y_down_left), cv2.FONT_HERSHEY_COMPLEX, size_text, color,
                    size_letters)
        cv2.putText(self.main_card, weather, (self.width_main_card // 3, Y + 30), cv2.FONT_HERSHEY_COMPLEX, size_text,
                    color,
                    size_letters)
        cv2.putText(self.main_card, temper, (self.width_main_card // 3, Y + 60), cv2.FONT_HERSHEY_COMPLEX, size_text,
                    color,
                    size_letters)

    def create_main_card(self):
        self.main_card = cv2.imread(self.path_card_main)
        self.width_main_card = 800
        self.height_main_card = 400
        self.size_main_card = (self.width_main_card, self.height_main_card)
        self.main_card = cv2.resize(self.main_card, self.size_main_card, interpolation=cv2.INTER_AREA)

    def weather_picture(self, path_picture):
        self.weather_card = cv2.imread(path_picture)
        self.width_weather_card = self.weather_card.shape[1]
        self.height_weather_card = self.weather_card.shape[0]
        self.size_weather_card = (self.width_weather_card, self.height_weather_card)
        self.weather_card = cv2.resize(self.weather_card, self.size_weather_card, interpolation=cv2.INTER_AREA)

    def gluing(self):
        dx = self.width_main_card - self.width_weather_card
        for x in range(self.width_weather_card):
            for y in range(self.height_weather_card):
                self.main_card[y, x + dx] = self.weather_card[y, x]




    def background_coloring(self, colour):
        max_ = max(colour[0], colour[1], colour[2])
        dx_const = math.ceil((self.width_main_card / max_))
        X,Y,Z = colour
        X_NEW, Y_NEW, Z_NEW = 255, 255, 255
        for x in range(0, self.width_main_card, dx_const):
            self.main_card[:, x:x+dx_const] = [X_NEW, Y_NEW, Z_NEW]
            if X == Y == Z:
                X_NEW -= 1
                Y_NEW -= 1
                Z_NEW -= 1
            else:
                if X == 0:
                    X_NEW -= 1
                if Y == 0:
                    Y_NEW -= 1
                if Z == 0:
                    Z_NEW -= 1


    def schow_card(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    matrix_weather = WeatherMaker().run()
    pprint(matrix_weather)
    picture = ImageMaker(day='1.10.2020', matrix_weather=matrix_weather).run()