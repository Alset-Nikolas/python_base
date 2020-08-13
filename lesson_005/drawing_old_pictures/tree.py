# -*- coding: utf-8 -*-
def tree_draw():
    import simple_draw as sd
    sd.resolution = (1200, 800)

    start = sd.Point(600, 50)

    def draw_branches(point_start, angle, length):
        if length < 10:
            return
        angle_alfa = sd.random_number(0.6 * 30, 1.4 * 30)
        sigma = sd.random_number(8, 12) / 10
        branches = sd.Vector(start_point=point_start, direction=angle, length=length)
        draw_branches(point_start=branches.end_point, angle=angle + angle_alfa, length=length * 0.75 * sigma)
        draw_branches(point_start=branches.end_point, angle=angle - angle_alfa, length=length * 0.75 * sigma)
        branches.draw(width=3)

    draw_branches(start, 90, 150)
    sd.pause()


if __name__ == '__main__':
    tree_draw()
