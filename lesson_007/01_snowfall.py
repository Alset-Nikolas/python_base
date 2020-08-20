# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 800)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.start_x = sd.random_number(0, 800)
        self.start_y = sd.random_number(0, 800)
        self.start_point = sd.Point(self.start_x, self.start_y)
        self.snowfall_length = sd.random_number(5, 10)
        self.flag_can_fall = False

    def move(self):
        if self.start_y - self.snowfall_length >= 0:
            self.start_x += sd.random_number(-2, 2)
            self.start_y -= sd.random_number(5, 15)
            self.start_point = sd.Point(self.start_x, self.start_y)
        else:
            self.flag_can_fall = True
            self.start_y -= 0
            self.start_point = sd.Point(self.start_x, self.start_y)

    def draw(self):
        sd.snowflake(center=self.start_point, length=self.snowfall_length, color=sd.COLOR_WHITE)

    def clear_previous_picture(self):
        sd.snowflake(center=self.start_point, length=self.snowfall_length, color=sd.background_color)

    def can_fall(self):
        if self.flag_can_fall:
            return False
        return True


# TODO, в этом месте итерация лишняя. Обычно она используется для НЕсоздания списка.
#  В памяти только 1 элемент, способ получения второго и условие окончания итераций.
#  Получается список мы всё равно используем. Значит инетатор только усложнил код.
#  У Вас без итераций не получилось?
class Snowflakes():
    def __init__(self):
        self.snowflakes = []
        self.len = 0
        self.all_fall_snowflakes = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.len:
            self.index += 1
            return self.snowflakes[self.index - 1]
        else:
            self.index = 0
            raise StopIteration

    def get_flakes(self, count):
        self.snowflakes = [Snowflake() for x in range(count)]
        self.len += count

    def get_fallen_flakes(self):
        count = 0
        for snowflake in self.snowflakes:
            if snowflake.flag_can_fall:
                count += 1
        new_fall_snowflakes = count - self.all_fall_snowflakes
        self.all_fall_snowflakes = count
        return new_fall_snowflakes

    def append_flakes(self, count):
        for _ in range(count):
            self.snowflakes.append(Snowflake())
        self.len += count


N = 10
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = Snowflakes()  # создать список снежинок
flakes.get_flakes(N)
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = flakes.get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        flakes.append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
