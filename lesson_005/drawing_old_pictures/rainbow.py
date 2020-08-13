# -*- coding: utf-8 -*-
def rainbow_picture(x_center=600, y_center=0, radius=500):
    import simple_draw as sd

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    center_position = sd.Point(x_center, y_center)

    for color in rainbow_colors[::-1]:
        sd.circle(center_position, radius=radius, color=color, width=10)
        radius += 10
    sd.pause()


if __name__ == '__main__':
    rainbow_picture(x_center=600, y_center=0, radius=500)
    sd.pause()
