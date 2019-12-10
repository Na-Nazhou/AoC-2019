#!/usr/bin/env python3

# python3 day4pt2.py 357253 892942

import sys


def main():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    count = 0
    for i in range(start, end + 1):
        double = False
        repeatcount = 0
        nondecrease = True
        string = str(i)
        for j in range(1, 6):
            if string[j] == string[j - 1]:
                repeatcount += 1
            elif repeatcount == 1:
                double = True
            else:
                repeatcount = 0  # reset counter

            if int(string[j]) < int(string[j - 1]):
                nondecrease = False
                break

        if (double or repeatcount == 1) and nondecrease:
            count += 1
    print(count)  # output


if __name__ == "__main__":
    main()
