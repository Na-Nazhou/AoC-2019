#!/usr/bin/env python3

import sys
import copy
from day12util import extract


def get_initial_state():
    initial_state = [[] for i in range(3)]
    for line in sys.stdin:
        state = extract(line)
        for i, axis in enumerate(initial_state):
            axis.append([state[i], 0])
    return initial_state


def update_state(curr_state):
    # update velocity
    for moon in curr_state:
        moon_pos = moon[0]
        for other in curr_state:
            if other != moon:
                other_pos = other[0]
                if moon_pos < other_pos:
                    moon[1] += 1
                elif moon_pos > other_pos:
                    moon[1] -= 1

    # update position
    for moon in curr_state:
        moon[0] += moon[1]


def get_repeat(curr_state):
    history = dict()
    i = 0
    while True:
        if str(curr_state) in history:
            return i
        else:
            history[str(curr_state)] = i
        update_state(curr_state)
        i += 1


def get_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def get_lcm(x, y):
    return x * y // get_gcd(x, y)


def main():
    initial_state = get_initial_state()
    repeats = []
    for axis in initial_state:
        repeats.append(get_repeat(axis))
    x, y, z = repeats
    print(get_lcm(get_lcm(x, y), z))


if __name__ == "__main__":
    main()
