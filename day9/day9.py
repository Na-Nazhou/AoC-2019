#!/usr/bin/env python3

import sys


def set_value(memory, idx):
    if idx < 0:
        print("Invalid memory access")
    if idx not in memory.keys():
        memory[idx] = 0


def get_param_idx(memory, idx, mode, base):
    if mode in [0, 2]:
        if mode == 0:
            offset = 0
        elif mode == 2:
            offset = base
        set_value(memory, idx)
        return memory[idx] + offset
    elif mode == 1:
        return idx


def get_param(memory, idx, mode, base):
    param_idx = get_param_idx(memory, idx, mode, base)
    set_value(memory, param_idx)
    return memory[param_idx]


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


def main():
    memory = {
        idx: int(value) for idx, value in enumerate(sys.stdin.readline().strip().split(","))
    }
    memory[1000] = 0
    memory[63] = 0
    i = 0
    base = 0
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
            memory[get_param_idx(memory, i + 3, A, base)] = result
            i += 4
        if DE == 3:
            param_idx = get_param_idx(memory, i + 1, C, base)
            memory[param_idx] = int(input())  # additional input
            i += 2
        if DE == 4:
            param1 = get_param(memory, i + 1, C, base)
            print(param1)  # output
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


if __name__ == "__main__":
    main()