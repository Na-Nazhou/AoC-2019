import sys


def read():
    return {
        idx: int(value) for idx, value in enumerate(sys.stdin.readline().strip().split(","))
    }


def update(curr, direction):
    if direction == 'U':
        curr[1] += 1
    if direction == 'D':
        curr[1] -= 1
    if direction == 'R':
        curr[0] += 1
    if direction == 'L':
        curr[0] -= 1
