#!/usr/bin/env python3

# list is unhashable
# tuple is immutable

import sys


def update(curr, path):
    direction = path[0]
    if direction == 'U':
        curr[1] = curr[1] + 1
    if direction == 'D':
        curr[1] = curr[1] - 1
    if direction == 'R':
        curr[0] = curr[0] + 1
    if direction == 'L':
        curr[0] = curr[0] - 1


def main():
    w1 = sys.stdin.readline().strip().split(",")
    w2 = sys.stdin.readline().strip().split(",")
    points = {}
    min_steps = 10e9
    curr = [0, 0]
    count = 0
    for path in w1:
        length = int(path[1:])
        for i in range(length):
            update(curr, path)
            count += 1
            points[tuple(curr)] = count
    curr = [0, 0]  # reset the central port
    count = 0  # reset the counter
    for path in w2:
        length = int(path[1:])
        for i in range(length):
            update(curr, path)
            count += 1
            if tuple(curr) in points:
                min_steps = min(points[tuple(curr)] + count, min_steps)
    print(min_steps)  # output


if __name__ == "__main__":
    main()
