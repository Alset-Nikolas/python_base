# -*- coding: utf-8 -*-


def wall_draw(x_coordinates_down=0, y_coordinates_down=0, x_coordinates_up=700, y_coordinates_up=700):
    import simple_draw as sd

    def collorlinw_wall(x_new):
        if x_new + x_size <= x_coordinates_up:
            point_list = [sd.Point(x_new, y_new),
                          sd.Point(x_new, y_new + y_size),
                          sd.Point(x_new + x_size, y_new + y_size),
                          sd.Point(x_new + x_size, y_new)]
            sd.polygon(point_list, color=sd.COLOR_DARK_RED, width=0)

    def line_wall_draw(x_start, y_new, x_size, y_size, i):
        left_bottom = sd.Point(x_coordinates_down, y_coordinates_down)
        right_top = sd.Point(x_coordinates_down + x_size, y_coordinates_down + y_size)

        for x_new in range(x_start, x_coordinates_up, x_size):
            sd.rectangle(left_bottom, right_top, color=sd.COLOR_ORANGE, width=3)

            collorlinw_wall(x_new)

            left_bottom = sd.Point(x_new, y_new)
            right_top = sd.Point(x_size + x_new, y_size + y_new)
        return left_bottom

    def small_brick(x_start, y_start, y_size):
        x_size = x_coordinates_up - x_start
        left_bottom = sd.Point(x_start, y_start)
        right_top = sd.Point(x_start + x_size, y_start + y_size)

        point_list = [sd.Point(x_start, y_start),
                      sd.Point(x_start, y_start + y_size),
                      sd.Point(x_start + x_size, y_start + y_size),
                      sd.Point(x_start + x_size, y_start)]
        sd.polygon(point_list, color=sd.COLOR_DARK_RED, width=0)

        sd.rectangle(left_bottom, right_top, color=sd.COLOR_ORANGE, width=3)

    x_size, y_size = (x_coordinates_up - x_coordinates_down) // 5, (y_coordinates_up - y_coordinates_down) // 10

    for i, y_new in enumerate(range(y_coordinates_down, y_coordinates_up, y_size)):
        if i % 2 == 0:
            x_start = x_coordinates_down
            left_bottom = line_wall_draw(x_start, y_new, x_size, y_size, i)


        else:
            small_brick(x_coordinates_down, y_new, y_size)
            x_start = x_coordinates_down + x_size // 2
            left_bottom = line_wall_draw(x_start, y_new, x_size, y_size, i)

        dx_the_error_of_division = 1
        if x_coordinates_up - left_bottom.x - x_size // 2 >= dx_the_error_of_division:
            small_brick(left_bottom.x, left_bottom.y, y_size)


if __name__ == '__main__':
    import simple_draw as sd

    wall_draw(x_coordinates_down=100, y_coordinates_down=200, x_coordinates_up=500, y_coordinates_up=500)
    sd.pause()
