# -*- coding: utf-8 -*-
def smile_draw():
    import random
    import simple_draw as sd

    def pupil(point_eye_left, radius_eye, color=sd.COLOR_DARK_PURPLE):
        radius_pupil = radius_eye / 2
        x_center_eye_left = int(point_eye_left.x + radius_eye * 1.1 / 3)
        y_center_eye_left = int(point_eye_left.y - radius_eye * 1.1 / 3)
        point_eye_left = sd.Point(x_center_eye_left, y_center_eye_left)
        sd.circle(point_eye_left, radius=radius_pupil, color=color, width=0)

    def eye_left(point, radius, color=sd.COLOR_DARK_PURPLE):
        radius_eye = radius / 5
        x_center_eye_left = int(point.x - radius * 1.3 / 3)
        y_center_eye_left = int(point.y + radius * 1.3 / 3)
        point_eye_left = sd.Point(x_center_eye_left, y_center_eye_left)
        sd.circle(point_eye_left, radius=radius_eye, color=color, width=3)
        pupil(point_eye_left, radius_eye, color=color)

    def eye_right(point, radius, color=sd.COLOR_DARK_PURPLE):
        radius_eye = radius / 5
        x_center_eye_left = int(point.x + radius * 1.3 / 3)
        y_center_eye_left = int(point.y + radius * 1.3 / 3)
        point_eye_right = sd.Point(x_center_eye_left, y_center_eye_left)
        sd.circle(point_eye_right, radius=radius_eye, color=color, width=3)
        pupil(point_eye_right, radius_eye, color=color)

    def grin(point, radius, color=sd.COLOR_DARK_PURPLE):
        x_smile = point.x
        y_smile = point.y
        x_point_1 = x_smile - radius / 3
        x_point_2 = x_smile
        x_point_3 = x_smile + radius / 3
        y_point_1 = y_smile - radius / 3
        y_point_2 = y_smile - radius / 2
        y_point_3 = y_smile - radius / 3
        point_list = [sd.Point(x_point_1, y_point_1), sd.Point(x_point_2, y_point_2), sd.Point(x_point_3, y_point_3)]
        sd.lines(point_list, color=color, closed=False, width=3)

    def smile(x_coordinates=300, y_coordinates=300, color=sd.COLOR_DARK_PURPLE, radius=30):
        point = sd.Point(x_coordinates, y_coordinates)
        sd.circle(point, radius=radius, color=color, width=3)
        eye_left(point=point, radius=radius, color=color)
        eye_right(point=point, radius=radius, color=color)
        grin(point=point, radius=radius, color=color)

    for _ in range(10):
        x = random.randint(50, 600)
        y = random.randint(50, 600)
        smile(x, y, color=sd.COLOR_DARK_PURPLE)
    sd.pause()


if __name__ == '__main__':
    smile_draw()
