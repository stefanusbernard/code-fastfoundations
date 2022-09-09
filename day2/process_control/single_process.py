import multiprocessing
import os

import sys


def calculate_geometric_series(a, r, n=10):
    print(f"child process: {os.getpid() = }")
    if r == 1:
        print(f"s_{n}({a = }, {r = } = {a * (n + 1)}")
    else:
        print(f"s_{n}({a = }, {r = } = {a * (1 - r ** (n + 1)) / (1 - r)}")


def main():
    print(f"parent process: {os.getpid() = }")
    process = multiprocessing.Process(
        name='calculate_geometric_series',
        target=calculate_geometric_series,
        args=(2, 0.333333333, 1000)
    )
    # process.daemon = True # to run in the background
    process.start()
    process.join()  # if daemon then no need to join
    return 0


if __name__ == "__main__":
    sys.exit(main())
