import queue
from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def bfs(src, memory):
    p = dict()
    q = queue.Queue()
    q.put((src, IntCodeComputer(memory)))

    while not q.empty():
        u, intcode = q.get()
        neighbors = [(u[0], u[1] + 1), (u[0], u[1] - 1),
                     (u[0] - 1, u[1]), (u[0] + 1, u[1])]
        for idx, neighbor in enumerate(neighbors):
            if neighbor not in p:
                p[neighbor] = u
                copy = intcode.copy()
                copy.read(idx + 1)
                copy.run()
                while not copy.output.empty():
                    status = copy.output.get()
                    if status == 2:
                        return (neighbor, p)
                    elif status == 1:
                        q.put((neighbor, copy))


def main():
    memory = read()
    src = (0, 0)
    dest, p = bfs(src, memory)
    count = 0
    curr = dest
    while curr != src:
        count += 1
        curr = p[curr]
    print(count)


if __name__ == "__main__":
    main()
