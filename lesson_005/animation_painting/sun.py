# -*- coding: utf-8 -*-

def sun_draw(x_center, y_center, Radius, delta=0):
    import simple_draw as sd

    center_position = sd.Point(x_center, y_center)
    sd.circle(center_position, radius=2 * Radius + 5, color=sd.background_color, width=0)
    sd.circle(center_position, radius=Radius, color=sd.COLOR_YELLOW, width=0)
    sd.circle(center_position, radius=Radius, color=sd.COLOR_ORANGE, width=2)

    betta = sd.random_number(5, 10)
    for alfa in range(delta, 360 + delta, betta):
        sd.line(center_position, sd.Point(x_center + 2 * Radius * sd.cos(alfa), y_center + 2 * Radius * sd.sin(alfa)))
    delta += 5
    return delta


if __name__ == '__main__':
    import simple_draw as sd

    X_SIZE = 1200

    sun_draw(300, 300, 50)
    sd.pause()
