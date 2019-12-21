#!/usr/bin/env python3

import sys
from day12util import extract

# test1: python3 day12pt1.py 10 < day12/test1.in
# test2: python3 day12pt1.py 100 < day12/test2.in
# actual data: python3 day12pt1.py 1000 < day12/data.in


def main():
    moons = []
    for line in sys.stdin:
        pos = extract(line)
        moons.append([pos, [0, 0, 0]])
    for i in range(int(sys.argv[1])):
        # update velocity
        for moon in moons:
            moon_pos = moon[0]
            for other in moons:
                if other != moon:
                    other_pos = other[0]
                    for axis, pos in enumerate(moon_pos):
                        if pos < other_pos[axis]:
                            moon[1][axis] += 1
                        elif pos > other_pos[axis]:
                            moon[1][axis] -= 1
        # update position
        for moon in moons:
            moon_velocity = moon[1]
            for axis, velocity in enumerate(moon_velocity):
                moon[0][axis] += velocity

    total = 0
    for moon in moons:
        pot = 0
        kin = 0
        moon_pos = moon[0]
        for pos in moon_pos:
            pot += abs(pos)
        moon_velocity = moon[1]
        for velocity in moon_velocity:
            kin += abs(velocity)
        total += pot * kin
    print(total)  # output


if __name__ == "__main__":
    main()
