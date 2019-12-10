#!/usr/bin/env python3

import sys


def main():
    image = [int(x) for x in sys.stdin.readline().strip()]
    arr = []
    step = 25 * 6  # additional input
    min_zero = 10e9
    for i in range(0, len(image), step):
        temp = image[i: i + step]
        arr.append(temp)

    for layer in arr:
        count_zero = 0
        for digit in layer:
            if digit == 0:
                count_zero += 1
        if count_zero < min_zero:
            min_zero = count_zero
            min_layer = layer

    count_one = 0
    count_two = 0
    for digit in min_layer:
        if digit == 1:
            count_one += 1
        if digit == 2:
            count_two += 1

    print(count_one * count_two)  # output


if __name__ == "__main__":
    main()
