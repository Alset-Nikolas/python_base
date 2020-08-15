from random import randint

ALL_PROBE = set()


def maybe_the_right_number():
    global ALL_PROBE

    power_dictionary = len(ALL_PROBE)
    while power_dictionary == len(ALL_PROBE):
        variant = [None] * 4

        while len(variant) != len(set(variant)):
            variant = [randint(1, 9), randint(0, 9), randint(0, 9), randint(0, 9)]

        variant = str(variant[0]) + str(variant[1]) + str(variant[2]) + str(variant[3])
        ALL_PROBE.add(variant)

    return variant
