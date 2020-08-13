# -*- coding: utf-8 -*-

def snowfall_draw():
    import simple_draw as sd

    sd.resolution = (700, 700)
    N = 20

    sd.start_drawing()
    sd.finish_drawing()

    start_x = [0] * N
    start_y = [0] * N
    snowfall_length = [0] * N
    start_point = [0] * N
    flag_add_new_snowfall = [0] * N
    for i in range(N):
        start_x[i] = sd.random_number(100, 600)
        start_y[i] = sd.random_number(100, 600)
        snowfall_length[i] = sd.random_number(10, 30)
        start_point[i] = sd.Point(start_x[i], start_y[i])

    def add_snowfall():
        start_x.append(sd.random_number(100, 600))
        start_y.append(sd.random_number(100, 600))
        snowfall_length.append(sd.random_number(10, 30))
        start_point.append(sd.Point(start_x[i], start_y[i]))
        flag_add_new_snowfall.append(0)

    while True:
        sd.start_drawing()

        for i in range(N):
            sd.snowflake(center=start_point[i], length=snowfall_length[i], color=sd.background_color)
            if start_y[i] - snowfall_length[i] <= 0 and flag_add_new_snowfall[i] == 0:
                add_snowfall()
                N += 1
                flag_add_new_snowfall[i] = 1
            elif start_y[i] - snowfall_length[i] <= 0 and flag_add_new_snowfall[i] == 1:
                start_y[i] -= 0
                start_x[i] -= 0
            else:
                start_y[i] -= sd.random_number(1, 5)
                start_x[i] -= sd.random_number(-2, 2)
            start_point[i] = sd.Point(start_x[i], start_y[i])
            sd.snowflake(center=start_point[i], length=snowfall_length[i], color=sd.COLOR_WHITE)

        sd.sleep(0.1)

        if sd.user_want_exit():
            break
        sd.finish_drawing()


if __name__ == '__main__':
    snowfall_draw()
