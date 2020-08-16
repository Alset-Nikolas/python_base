import simple_draw as sd


def street_draw(X_SIZE, dy):
    point_list = [sd.Point(0, 0),
                  sd.Point(0, dy),
                  sd.Point(X_SIZE, dy),
                  sd.Point(X_SIZE, 0)]
    sd.polygon(point_list, color=sd.COLOR_DARK_GREEN, width=0)

    sd.polygon(point_list, color=sd.COLOR_BLACK, width=3)


if __name__ == '__main__':
    import simple_draw as sd

    X_SIZE = 1200

    street_draw(X_SIZE, 200)
    sd.pause()
