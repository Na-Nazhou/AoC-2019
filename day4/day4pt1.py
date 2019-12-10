#!/usr/bin/env python3

# python3 day4pt1.py 357253 892942

import sys


def main():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    count = 0
    for i in range(start, end + 1):
        double = False
        nondecrease = True
        string = str(i)
        for j in range(1, len(string)):
            if string[j] == string[j - 1]:
                double = True
            if int(string[j]) < int(string[j - 1]):
                nondecrease = False
                break
        if double and nondecrease:
            count += 1
    print(count)  # output


if __name__ == "__main__":
    main()
