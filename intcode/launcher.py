from .util import read
from .util import run


def launch():
    memory = read()
    run(memory)
