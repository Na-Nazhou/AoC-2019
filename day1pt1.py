#!/usr/bin/env python3

import sys


def main():
    sum = 0
    for line in sys.stdin:
        sum += int(line) // 3 - 2
    print(sum)  # output


if __name__ == "__main__":
    main()
