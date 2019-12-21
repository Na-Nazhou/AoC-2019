import queue
from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def bfs(memory):
    walls = set()
    p = dict()
    q = queue.Queue()
    intcode = IntCodeComputer(memory)
    q.put(((0, 0), intcode))

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
                    if status == 0:
                        walls.add(neighbor)
                    elif status == 2:
                        return (neighbor, p)
                    elif status == 1:
                        q.put((neighbor, copy))


def main():
    memory = read()
    dest, p = bfs(memory)
    count = 0
    curr = dest
    while curr != (0, 0):
        count += 1
        curr = p[curr]
    print(count)


if __name__ == "__main__":
    main()
