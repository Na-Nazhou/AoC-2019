import sys
import math

# test1: python3 day16pt1.py 4 < day16/test1.in
# test2: python3 day16pt1.py 100 < day16/test2.in
# test3: python3 day16pt1.py 100 < day16/test3.in
# test4: python3 day16pt1.py 100 < day16/test4.in
# actual data: python3 day16pt1.py 100 < day16/data.in


def process(curr_index, length, index, repeat):
    lst = []
    counter = 0
    while curr_index < length:
        lst.append(curr_index)
        counter += 1
        if counter == index + 1:
            curr_index += (repeat - counter + 1)
            counter = 0
        else:
            curr_index += 1
    return lst


def get_pattern(index, length, mem):
    if index in mem:
        return mem[index]

    repeat = (index + 1) * 4
    plus_start = index
    minus_start = 3 * index + 2
    plus = process(plus_start, length, index, repeat)
    minus = process(minus_start, length, index, repeat)
    mem[index] = (plus, minus)
    return (plus, minus)


def get_digit(index, phase, input_list, pattern_mem, mem):
    if (phase, index) in mem:
        return mem[(phase, index)]

    if phase == 0:
        result = input_list[index]
    else:
        plus, minus = get_pattern(index, len(input_list), pattern_mem)
        result = 0
        for idx in plus:
            result += get_digit(idx, phase - 1, input_list, pattern_mem, mem)
        for idx in minus:
            result -= get_digit(idx, phase - 1, input_list, pattern_mem, mem)
        result = abs(result) % 10
    mem[(phase, index)] = result
    return result


def main():
    input_list = [int(i) for i in sys.stdin.read().strip()]
    mem = {}
    pattern_mem = {}
    for i in range(8):
        print(
            str(get_digit(i, int(sys.argv[1]), input_list, pattern_mem, mem)), end="")
    print()


if __name__ == "__main__":
    main()
