# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall

# На основе кода из lesson_004/05_snowfall.py
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
snowfall.create_snowfall(20)

while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    snowfall.draw_snowfall(color=sd.background_color)
    #  сдвинуть_снежинки()
    snowfall.dy_snowfall()
    #  нарисовать_снежинки_цветом(color)
    snowfall.draw_snowfall(color=sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то
    res = snowfall.exit_border_snowfall()
    if res:
        snowfall.del_snowfall(res)
        #       удалить_снежинки(номера)
        snowfall.create_snowfall(len(res))
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачёт! 🚀
