# -*- coding: utf-8 -*-
def rainbow_picture():
    import simple_draw as sd

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    radius = 550
    center_position = sd.Point(600, 0)

    for color in rainbow_colors[::-1]:
        sd.circle(center_position, radius=radius, color=color, width=10)
        radius += 10
    sd.pause()


if __name__ == '__main__':
    rainbow_picture()
