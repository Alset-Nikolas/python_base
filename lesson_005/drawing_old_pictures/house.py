from lesson_005.drawing_old_pictures.wall import wall_draw
def hose_draw(x_left_down = 300, x_size = 400, y_size = 300, y_left_down = 200):

    import simple_draw as sd



    def roof():
        point_list = [sd.Point(x_left_down-10, y_left_down+y_size-5),
                      sd.Point((x_left_down+x_left_down+x_size)//2, y_left_down+y_size+y_size//2),
                      sd.Point(x_left_down+x_size+10, y_left_down+y_size-5),
                      sd.Point(x_left_down-10, y_left_down+y_size-5)]
        sd.polygon(point_list, color=sd.COLOR_YELLOW, width=0)



    def window():
        center_position = sd.Point((x_left_down+x_left_down+x_size)//2, (y_left_down+y_left_down+y_size)//2)
        sd.circle(center_position, radius=y_size//3, color=sd.background_color, width=0)
        sd.circle(center_position, radius=y_size // 3, color=sd.COLOR_ORANGE, width=2)
        sd.line(start_point=sd.Point((x_left_down+x_left_down+x_size)//2, (y_left_down+y_left_down+y_size)//2-y_size // 3),
                end_point=sd.Point((x_left_down+x_left_down+x_size)//2,(y_left_down+y_left_down+y_size)//2+y_size // 3),
                width=2,color=sd.COLOR_ORANGE,)

    sd.resolution = (1200, 800)
    wall_draw(x_coordinates_down=x_left_down, y_coordinates_down=y_left_down,
              x_coordinates_up=x_left_down+x_size, y_coordinates_up=y_left_down+y_size)
    window()
    roof()
    sd.pause()

if __name__ == '__main__':
    hose_draw()