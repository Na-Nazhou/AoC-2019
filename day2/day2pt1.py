#!/usr/bin/env python3

import sys


def main():
    arr = [int(x) for x in sys.stdin.readline().strip().split(",")]
    for x in range(0, len(arr), 4):
        if arr[x] == 99:
            break
        if arr[x] == 1:
            arr[arr[x + 3]] = arr[arr[x + 1]] + arr[arr[x + 2]]
        if arr[x] == 2:
            arr[arr[x + 3]] = arr[arr[x + 1]] * arr[arr[x + 2]]
    print(arr[0])  # output


if __name__ == "__main__":
    main()
