# -*- coding: utf-8 -*-

def sun_draw(x_center, y_center, Radius):
    import simple_draw as sd
    center_position = sd.Point(x_center, y_center)
    sd.circle(center_position, radius=Radius, color=sd.COLOR_YELLOW, width=0)
    sd.circle(center_position, radius=Radius, color=sd.COLOR_ORANGE, width=2)

    L= 2 * Radius
    for alfa in range(0, 360, 5):
        sd.line(center_position, sd.Point(x_center + L * sd.cos(alfa), y_center + L * sd.sin(alfa)))

if __name__ == '__main__':
    import simple_draw as sd

    X_SIZE = 1200

    sun_draw(300, 300, 50)
    sd.pause()
