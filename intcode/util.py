import sys


def read():
    return {
        idx: int(value) for idx, value in enumerate(sys.stdin.readline().strip().split(","))
    }
