#!/usr/bin/env python3

import sys
import copy


def main():
    arr = [int(x) for x in sys.stdin.readline().strip().split(",")]
    arr_copy = copy.deepcopy(arr)
    for i in range(100):
        for j in range(100):
            arr[1] = i
            arr[2] = j
            for x in range(0, len(arr), 4):
                if arr[x] == 99:
                    break
                if arr[x] == 1:
                    arr[arr[x + 3]] = arr[arr[x + 1]] + arr[arr[x + 2]]
                if arr[x] == 2:
                    arr[arr[x + 3]] = arr[arr[x + 1]] * arr[arr[x + 2]]
            if arr[0] == 19690720:  # additional input
                print(100 * i + j)  # output
                return
            arr = copy.deepcopy(arr_copy)


if __name__ == "__main__":
    main()
