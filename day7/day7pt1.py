#!/usr/bin/env python3

import sys
import copy
import itertools as it


def get_param(arr, idx, mode):
    if mode == 0:
        return arr[arr[idx]]
    elif mode == 1:
        return arr[idx]


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


def get_output(arr_copy, input1, input2):
    arr = copy.deepcopy(arr_copy)
    i = 0
    isFirst = True
    while i < len(arr):
        opcode = arr[i]
        DE = opcode % 100
        C = (opcode // 100) % 10
        B = (opcode // 1000) % 10
        A = opcode // 10000
        if DE == 99:
            i += 1
            break
        if DE in [1, 2, 7, 8]:
            param1 = get_param(arr, i + 1, C)
            param2 = get_param(arr, i + 2, B)
            result = get_result(param1, param2, DE)
            arr[arr[i + 3]] = result
            i += 4
        if DE == 3:
            result = input2
            if isFirst:
                result = input1
                isFirst = False
            arr[arr[i + 1]] = result
            i += 2
        if DE == 4:
            param1 = get_param(arr, i + 1, C)
            i += 2
            return param1
        if DE in [5, 6]:
            param1 = get_param(arr, i + 1, C)
            if get_jump(param1, DE):
                param2 = get_param(arr, i + 2, B)
                i = param2
            else:
                i += 3


def main():
    arr = [int(x) for x in sys.stdin.readline().strip().split(",")]
    perms = list(it.permutations(range(5)))
    max_signal = -10e9
    for perm in perms:
        for idx, ipt in enumerate(perm):
            if idx == 0:
                output = get_output(arr, ipt, 0)
            else:
                output = get_output(arr, ipt, output)
        max_signal = max(output, max_signal)
    print(max_signal)  # output


if __name__ == "__main__":
    main()
