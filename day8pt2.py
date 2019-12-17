#!/usr/bin/env python3

import sys


def main():
    image = sys.stdin.readline().strip()
    arr = []
    step = 25 * 6  # additional input
    result = ['2' for i in range(step)]
    for i in range(0, len(image), step):
        temp = image[i:i + step]
        arr.append(temp)

    for layer in arr:
        for idx, digit in enumerate(layer):
            if result[idx] == '2' and digit != '2':
                result[idx] = digit

    for i in range(0, len(result), 25):
        for ch in result[i: i + 25]:
            if ch == '1':
                print("*", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
