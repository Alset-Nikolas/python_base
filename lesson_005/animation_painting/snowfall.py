# -*- coding: utf-8 -*-

def snowfall_draw(x_coordinates_down=0, y_coordinates_down=0, x_coordinates_up=700, y_coordinates_up=700,
                  start_x=[], start_y=[], snowfall_length=[], flag_add_new_snowfall=[], N=20):
    import simple_draw as sd

    sd.start_drawing()

    start_x = start_x or [sd.random_number(x_coordinates_down, x_coordinates_up) for x in range(N)]
    start_y = start_y or [sd.random_number(y_coordinates_down, y_coordinates_up) for y in range(N)]
    snowfall_length = snowfall_length or [sd.random_number(5, 10) for l in range(N)]
    flag_add_new_snowfall = flag_add_new_snowfall or [0] * N

    start_point = [sd.Point(start_x[i], start_y[i]) for i in range(N)]

    def add_snowfall():
        start_x.append(sd.random_number(x_coordinates_down, x_coordinates_up))
        start_y.append(sd.random_number(y_coordinates_down, y_coordinates_up))
        snowfall_length.append(sd.random_number(5, 10))
        start_point.append(sd.Point(start_x[i], start_y[i]))
        flag_add_new_snowfall.append(0)

    for i in range(N):
        sd.snowflake(center=start_point[i], length=snowfall_length[i], color=sd.background_color)
        if start_y[i] - snowfall_length[i] <= y_coordinates_down and flag_add_new_snowfall[i] == 0:
            add_snowfall()
            N += 1
            flag_add_new_snowfall[i] = 1

        elif start_y[i] - snowfall_length[i] <= y_coordinates_down and flag_add_new_snowfall[i] == 1:
            start_y[i] -= 0
            start_x[i] -= 0
        else:
            start_y[i] -= sd.random_number(1, 5)
            start_x[i] -= sd.random_number(-2, 2)

        start_point[i] = sd.Point(start_x[i], start_y[i])
    for i in range(N):
        sd.snowflake(center=start_point[i], length=snowfall_length[i], color=sd.COLOR_WHITE)
    sd.sleep(0.1)

    sd.finish_drawing()

    return start_x, start_y, snowfall_length, flag_add_new_snowfall, N
