#!/usr/bin/env python3

from day10util import read
from day10util import check


def main():
    asteroids = read()
    max_detection = 0
    for asteroid in asteroids:
        count = 0
        for other in asteroids:
            if other != asteroid and check(asteroid, other, asteroids):
                count += 1
        max_detection = max(count, max_detection)
    print(max_detection)  # output


if __name__ == "__main__":
    main()
