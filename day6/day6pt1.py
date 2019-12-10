#!/usr/bin/env python3

import sys


def main():
    graph = {}
    total = 0
    for edge in sys.stdin:
        vertices = edge.strip().split(")")
        v1 = vertices[0]
        v2 = vertices[1]
        if v1 not in graph.keys():
            graph[v1] = None
        graph[v2] = v1

    for child, parent in graph.items():
        count = 0
        curr = parent
        while curr:
            count += 1
            curr = graph[curr]
        total += count
    print(total)  # output


if __name__ == "__main__":
    main()
