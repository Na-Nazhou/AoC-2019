#!/usr/bin/env python3

import sys

# test1: python3 day12pt1.py 10 < test1.in
# test2: python3 day12pt1.py 100 < test2.in
# data: python3 day12pt1.py 1000 < data.in


def extract(line):
    end = 0
    result = []
    line = line.strip()[1:-1].split(", ")
    for part in line:
        arg, val = part.split("=")
        result.append(int(val))
    return result


def main():
    moons = []
    for line in sys.stdin:
        pos = extract(line)
        moons.append([pos, [0, 0, 0]])
    for i in range(int(sys.argv[1])):
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
