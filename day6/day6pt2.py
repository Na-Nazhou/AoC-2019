#!/usr/bin/env python3

import sys
import queue


def add_neighbor(v1, v2, graph):
    graph.setdefault(v1, [])
    graph[v1].append(v2)


def bfs(graph, src, dest):
    p = {}
    p.setdefault(src)
    q = queue.Queue()
    q.put(src)
    while not q.empty():
        u = q.get()
        for neighbor in graph[u]:
            if neighbor not in p:
                p[neighbor] = u
                q.put(neighbor)
        if dest in p:
            break

    count = 0
    curr = dest
    while curr != src:
        count += 1
        curr = p[curr]
    return count


def main():
    graph = {}
    for edge in sys.stdin:
        v1, v2 = edge.strip().split(")")
        add_neighbor(v1, v2, graph)
        add_neighbor(v2, v1, graph)
        if v2 == 'YOU':  # additional input
            src = v1
        elif v2 == 'SAN':  # additional input
            dest = v1
    print(bfs(graph, src, dest))  # output


if __name__ == "__main__":
    main()
