import multiprocessing
import os
import sys
import time


def func1(lock):
    """Write to stdout"""
    lock.acquire()
    # with lock:
    print(f"message 1 from func1")
    lock.release()
    time.sleep(2)
    with lock:  # context manager version
        print(f"message 2 from func1")


def func2(lock):
    """Write to stdout"""
    with lock:
        print(f"message 1 from func2")
        time.sleep(1)
        print(f"message 2 from func2")


def main():
    lock = multiprocessing.Lock()
    proc1 = multiprocessing.Process(target=func1, args=(lock,))
    proc2 = multiprocessing.Process(target=func2, args=(lock,))
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
