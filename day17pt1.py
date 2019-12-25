from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def main():
    memory = read()
    intcode = IntCodeComputer(memory)
    intcode.run()
    curr = [0, 0]
    scaffolds = set()
    while not intcode.output.empty():
        value = intcode.output.get()
        # print(chr(value), end="")
        if value == 35:
            scaffolds.add(tuple(curr))
        if value == 10:
            curr[1] += 1
            curr[0] = 0
        else:
            curr[0] += 1

    alignment_params = 0
    for scaffold in scaffolds:
        if (scaffold[0] - 1, scaffold[1]) not in scaffolds:
            continue
        if (scaffold[0] + 1, scaffold[1]) not in scaffolds:
            continue
        if (scaffold[0], scaffold[1] - 1) not in scaffolds:
            continue
        if (scaffold[0], scaffold[1] + 1) not in scaffolds:
            continue
        alignment_params += (scaffold[0] * scaffold[1])
    print(alignment_params)


if __name__ == "__main__":
    main()
