# -*- coding: utf-8 -*-
def rainbow_picture(x_center=600, y_center=0, radius=500, first_color=0):
    import simple_draw as sd
    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

    rainbow_colors = rainbow_colors[first_color:] + rainbow_colors[:first_color]
    center_position = sd.Point(x_center, y_center)

    for color in rainbow_colors[::-1]:
        sd.circle(center_position, radius=radius, color=color, width=10)
        radius += 10


if __name__ == '__main__':
    import simple_draw as sd

    rainbow_picture(x_center=600, y_center=0, radius=500, first_color=2)
    sd.pause()
