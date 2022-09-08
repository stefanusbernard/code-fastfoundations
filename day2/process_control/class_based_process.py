import multiprocessing
import sys


class MyProcess(multiprocessing.Process):
    def run(self):
        """Define what should happen"""
        print('nothing')


def main():
    p = MyProcess()
    p.start()
    p.join()
    return 0


if __name__ == "__main__":
    sys.exit(main())
