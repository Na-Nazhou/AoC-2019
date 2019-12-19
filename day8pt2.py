#!/usr/bin/env python3

import sys
from util import draw


def main():
    image = sys.stdin.readline().strip()
    arr = []
    length = 25  # additional input
    width = 6  # additional input
    step = length * width
    result = ['2' for i in range(step)]
    for i in range(0, len(image), step):
        temp = image[i:i + step]
        arr.append(temp)

    for layer in arr:
        for idx, digit in enumerate(layer):
            if result[idx] == '2' and digit != '2':
                result[idx] = digit

    for i in range(0, len(result), length):
        for ch in result[i: i + length]:
            draw(ch == '1')
        print()


if __name__ == "__main__":
    main()
