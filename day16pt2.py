import sys
import math


def main():
    input_list = [int(i) for i in sys.stdin.read().strip()] * 10000
    message_offset = int("".join([str(i) for i in input_list[:7]]))

    for _ in range(100):
        for i in range(len(input_list) - 2, message_offset - 1, -1):
            input_list[i] = (input_list[i] + input_list[i + 1]) % 10

    for i in range(8):
        print(input_list[message_offset + i], end="")
    print()


if __name__ == "__main__":
    main()
