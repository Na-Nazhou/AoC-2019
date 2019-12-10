#!/usr/bin/env python3

import sys


def main():
    p = {}
    total = 0
    for edge in sys.stdin:
        v1, v2 = edge.strip().split(")")
        if v1 not in p.keys():
            p[v1] = None
        p[v2] = v1

    for child, parent in p.items():
        count = 0
        curr = parent
        while curr is not None:
            count += 1
            curr = p[curr]
        total += count
    print(total)  # output


if __name__ == "__main__":
    main()
