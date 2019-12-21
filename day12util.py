import sys


def extract(line):
    end = 0
    result = []
    line = line.strip()[1:-1].split(", ")
    for part in line:
        arg, val = part.split("=")
        result.append(int(val))
    return result
