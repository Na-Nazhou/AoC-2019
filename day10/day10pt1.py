#!/usr/bin/env python3

import sys


def in_range(x, a, b):
    return x >= min(a, b) and x <= max(a, b)


def same_line(a, b, c):
    ab_disp1 = a[0] - b[0]
    ab_disp2 = a[1] - b[1]
    bc_disp1 = c[0] - b[0]
    bc_disp2 = c[1] - b[1]
    if bc_disp1 == 0 or ab_disp1 == 0:
        return False
    return bc_disp2 / bc_disp1 == ab_disp2 / ab_disp1


def check(src, dest, arr):
    x_disp = dest[0] - src[0]
    for cell in arr:
        if cell == src or cell == dest:
            continue
        if x_disp != 0 and not same_line(cell, src, dest):
            continue
        if x_disp == 0 and cell[0] != src[0]:
            continue
        if in_range(cell[0], src[0], dest[0]) and in_range(cell[1], src[1], dest[1]):
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
        for other in asteroids:
            if other != asteroid and check(asteroid, other, asteroids):
                count += 1
        max_detection = max(count, max_detection)
    print(max_detection)


if __name__ == "__main__":
    main()
