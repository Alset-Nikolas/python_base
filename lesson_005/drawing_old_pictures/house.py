from lesson_005.drawing_old_pictures.wall import wall_draw
from lesson_005.drawing_old_pictures.smile import smile_draw
# TODO lesson_005. указывать не нужно


def hose_draw(x_left_down=100, x_size=400, y_size=200, y_left_down=200):
    import simple_draw as sd

    def roof():
        point_list = [sd.Point(x_left_down - 10, y_left_down + y_size - 5),
                      sd.Point((x_left_down + x_left_down + x_size) // 2, y_left_down + y_size + y_size // 2),
                      sd.Point(x_left_down + x_size + 10, y_left_down + y_size - 5),
                      sd.Point(x_left_down - 10, y_left_down + y_size - 5)]
        sd.polygon(point_list, color=sd.COLOR_DARK_PURPLE, width=0)
        sd.polygon(point_list, color=sd.COLOR_DARK_ORANGE, width=3)

    def window():
        center_position = sd.Point((x_left_down + x_left_down + x_size) // 2, (y_left_down + y_left_down + y_size) // 2)
        sd.circle(center_position, radius=y_size // 3, color=sd.background_color, width=0)
        sd.circle(center_position, radius=y_size // 3, color=sd.COLOR_ORANGE, width=2)
        sd.line(start_point=sd.Point((x_left_down + x_left_down + x_size) // 2,
                                     (y_left_down + y_left_down + y_size) // 2 - y_size // 3),
                end_point=sd.Point((x_left_down + x_left_down + x_size) // 2,
                                   (y_left_down + y_left_down + y_size) // 2 + y_size // 3),
                width=3, color=sd.COLOR_ORANGE)

        smile_draw(x_strart=center_position.x - y_size // 6, y_start=center_position.y)

    wall_draw(x_coordinates_down=x_left_down, y_coordinates_down=y_left_down,
              x_coordinates_up=x_left_down + x_size, y_coordinates_up=y_left_down + y_size)
    window()
    roof()


if __name__ == '__main__':
    import simple_draw as sd

    hose_draw()
    sd.pause()
