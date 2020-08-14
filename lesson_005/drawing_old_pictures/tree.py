# -*- coding: utf-8 -*-
import simple_draw as sd


def tree_draw(x_start, y_start, length, color=sd.COLOR_YELLOW):
    import simple_draw as sd
    sd.resolution = (1200, 800)

    start = sd.Point(x_start, y_start)

    def draw_branches(point_start, angle, length):
        if length < 10:
            return
        angle_alfa = sd.random_number(0.6 * 30, 1.4 * 30)
        sigma = sd.random_number(8, 12) / 10
        branches = sd.Vector(start_point=point_start, direction=angle, length=length)
        draw_branches(point_start=branches.end_point, angle=angle + angle_alfa, length=length * 0.75 * sigma)
        draw_branches(point_start=branches.end_point, angle=angle - angle_alfa, length=length * 0.75 * sigma)
        branches.draw(width=3, color=color)

    draw_branches(start, 90, length)


if __name__ == '__main__':
    import simple_draw as sd

    tree_draw(500, 100, 100)
    sd.pause()
