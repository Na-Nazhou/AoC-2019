#!/usr/bin/env python3

import sys
import math


def get_degree(src, dest):
    x_disp = dest[0] - src[0]
    y_disp = dest[1] - src[1]
    if x_disp == 0:
        if y_disp < 0:
            return 0
        else:
            return 180
    degree = math.atan(y_disp / x_disp) / math.pi * 180
    if x_disp > 0:
        return degree + 90
    if x_disp < 0:
        return degree + 270


def get_distance(src, dest):
    x_disp = dest[0] - src[0]
    y_disp = dest[1] - src[1]
    return math.sqrt(x_disp ** 2 + y_disp ** 2)


def check(src, dest, arr):
    for cell in arr:
        if cell == src or cell == dest:
            continue
        if get_degree(src, dest) == get_degree(src, cell) and get_distance(src, dest) > get_distance(src, cell):
            return False
    return True


def main():
    asteroids = []
    for j, line in enumerate(sys.stdin):
        for i, ch in enumerate(line):
            if ch == '#':
                asteroids.append((i, j))
    max_detection = 0
    for asteroid in asteroids:
        count = 0
        visible = {}
        for other in asteroids:
            if other != asteroid and check(asteroid, other, asteroids):
                count += 1
                visible[other] = get_degree(asteroid, other)
        if count > max_detection:
            max_detection = count
            monitored = visible

    sorted_asteroids = sorted(monitored.items(), key=lambda item: item[1])
    # Assumption: there are at least 200 asteroids that can be detected
    the200th = sorted_asteroids[199][0]
    print(the200th[0] * 100 + the200th[1])  # output


if __name__ == "__main__":
    main()
