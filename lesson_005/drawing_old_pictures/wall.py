# -*- coding: utf-8 -*-



def wall_draw(x_coordinates_down=0, y_coordinates_down=0, x_coordinates_up=700, y_coordinates_up=700):
    import simple_draw as sd

    sd.resolution = (1200, 800)

    def line_wall_draw(x_start, y_new, x_size, y_size):
        left_bottom = sd.Point(x_coordinates_down, y_coordinates_down)
        right_top = sd.Point(x_coordinates_down + x_size, y_coordinates_down + y_size)

        for x_new in range(x_start, x_coordinates_up, x_size):
            sd.rectangle(left_bottom, right_top, color=sd.COLOR_ORANGE, width=3)

            left_bottom = sd.Point(x_new, y_new)
            right_top = sd.Point(x_size + x_new, y_size + y_new)
        return left_bottom

    def small_brick(x_start, y_new, x_size, y_size):
        x_size //= 2
        left_bottom = sd.Point(x_start, y_new)
        right_top = sd.Point(x_start + x_size, y_new + y_size)
        sd.rectangle(left_bottom, right_top, color=sd.COLOR_ORANGE, width=3)

    x_size, y_size = (x_coordinates_up - x_coordinates_down) // 7, (y_coordinates_up - y_coordinates_down) // 14
    print(x_size, y_size)
    for i, y_new in enumerate(range(y_coordinates_down, y_coordinates_up, y_size)):





        if i % 2 == 0:
            x_start = x_coordinates_down
            left_bottom = line_wall_draw(x_start, y_new, x_size, y_size)

        else:
            small_brick(x_coordinates_down, y_new, x_size, y_size)
            x_start = x_coordinates_down + x_size // 2
            left_bottom = line_wall_draw(x_start, y_new, x_size, y_size)

        print(x_coordinates_up, left_bottom)
        dx_the_error_of_division = 5
        if x_coordinates_up-left_bottom.x >= x_size//2:
            print(x_coordinates_up-left_bottom.x )
            print(i)
            small_brick(left_bottom.x, left_bottom.y, x_size, y_size)

    sd.pause()


if __name__ == '__main__':
    wall_draw(x_coordinates_down=1, y_coordinates_down=200, x_coordinates_up=638, y_coordinates_up=700)

