import sys
import math

# test1: python3 day16pt1.py 4 < day16/test1.in
# test2: python3 day16pt1.py 100 < day16/test2.in
# test2: python3 day16pt1.py 100 < day16/test3.in
# test2: python3 day16pt1.py 100 < day16/test4.in
# actual data: python3 day16pt1.py 100 < day16/data.in


def get_pattern(base, phase, length):
    result = []
    counter = 0
    curr = 0
    while len(result) < length + 1:
        result.append(base[curr])
        counter += 1
        if counter == phase:
            counter = 0
            curr = (curr + 1) % len(base)
    return result[1:]


def main():
    base_pattern = [0, 1, 0, -1]
    input_list = [int(i) for i in sys.stdin.read().strip()]
    for i in range(int(sys.argv[1])):
        output = []
        for idx in range(len(input_list)):
            result = 0
            pattern = get_pattern(base_pattern, idx + 1, len(input_list))
            for i, val in enumerate(input_list):
                result += val * pattern[i]
            output.append(abs(result) % 10)
        input_list = output

    print("".join([str(i) for i in input_list])[:8])


if __name__ == "__main__":
    main()
