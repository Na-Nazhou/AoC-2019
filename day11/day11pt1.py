#!/usr/bin/env python3

import sys


def get_param_idx(memory, idx, mode, base):
    if mode in [0, 2]:
        if mode == 0:
            offset = 0
        elif mode == 2:
            offset = base
        return memory.get(idx, 0) + offset
    elif mode == 1:
        return idx


def get_param(memory, idx, mode, base):
    param_idx = get_param_idx(memory, idx, mode, base)
    return memory.get(param_idx, 0)


def get_result(param1, param2, DE):
    if DE == 1:
        return param1 + param2
    elif DE == 2:
        return param1 * param2
    elif DE == 7:
        return int(param1 < param2)
    elif DE == 8:
        return int(param1 == param2)


def get_jump(param, DE):
    if DE == 5:
        return param != 0
    elif DE == 6:
        return param == 0


def update(curr, face):
    directions = ['U', 'R', 'D', 'L']
    direction = directions[face]
    if direction == 'U':
        curr[1] = curr[1] + 1
    if direction == 'D':
        curr[1] = curr[1] - 1
    if direction == 'R':
        curr[0] = curr[0] + 1
    if direction == 'L':
        curr[0] = curr[0] - 1


def main():
    memory = {
        idx: int(value) for idx, value in enumerate(sys.stdin.readline().strip().split(","))
    }
    i = 0
    base = 0
    white_tiles = set()
    painted = set()
    curr = [0, 0]
    isFirst = True
    face = 0
    while True:
        opcode = memory[i]
        DE = opcode % 100
        C = (opcode // 100) % 10
        B = (opcode // 1000) % 10
        A = opcode // 10000
        if DE == 99:
            i += 1
            break
        if DE in [1, 2, 7, 8]:
            param1 = get_param(memory, i + 1, C, base)
            param2 = get_param(memory, i + 2, B, base)
            result = get_result(param1, param2, DE)
            param_idx = get_param_idx(memory, i + 3, A, base)
            memory[param_idx] = result
            i += 4
        if DE == 3:
            param_idx = get_param_idx(memory, i + 1, C, base)
            ipt = int(tuple(curr) in white_tiles)
            memory[param_idx] = ipt
            i += 2
        if DE == 4:
            param1 = get_param(memory, i + 1, C, base)
            if isFirst:
                if param1 == 1:
                    white_tiles.add(tuple(curr))
                elif param1 == 0 and tuple(curr) in white_tiles:
                    white_tiles.remove(tuple(curr))
                painted.add(tuple(curr))
            else:
                if param1 == 1:
                    face = (face + 5) % 4
                elif param1 == 0:
                    face = (face + 3) % 4
                update(curr, face)
            isFirst = not isFirst
            i += 2
        if DE in [5, 6]:
            param1 = get_param(memory, i + 1, C, base)
            if get_jump(param1, DE):
                param2 = get_param(memory, i + 2, B, base)
                i = param2
            else:
                i += 3
        if DE == 9:
            param1 = get_param(memory, i + 1, C, base)
            base += param1
            i += 2
    print(len(painted))  # output


if __name__ == "__main__":
    main()
