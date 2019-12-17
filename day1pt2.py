#!/usr/bin/env python3

import sys


def main():
    sum = 0
    for line in sys.stdin:
        curr = int(line)
        while (curr > 8):
            curr = curr // 3 - 2
            sum += curr
    print(sum)  # output


if __name__ == "__main__":
    main()
