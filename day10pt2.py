#!/usr/bin/env python3

from day10util import read
from day10util import check
from day10util import get_degree


def main():
    asteroids = read()
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
