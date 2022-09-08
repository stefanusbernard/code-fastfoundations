import multiprocessing
import os
import random
import sys


def generate_data(data_end):
    """generate data to be fed to workers"""
    for i in range(10):
        data_end.send(random.random())
    data_end.send(None)
    print("Inserted 10 items")
    data_end.close()


def work_on_data(input_end, output_end):
    """do something with the data and return results"""
    item_count = 0
    item = input_end.recv()
    while item is not None:
        print(f"Item {item}")
        output_end.send(item ** 2)
        item_count += 1
        item = input_end.recv()
    output_end.send(None)
    print(f"Worked on {item_count} items")
    input_end.close()


def present_results(result_end):
    """display the results"""
    item_count = 0
    item = result_end.recv()
    while item is not None:
        print(f"Final result: {item}")
        item_count += 1
        item = result_end.recv()
    print(f"Presented {item_count} items")
    result_end.close()  # close results


def main():
    """
    # a pipe has two ends:
    # - first one is sending data to the worker
    # - the second one is for sending results to the presenter
    """
    data_end, input_end = multiprocessing.Pipe()
    output_end, result_end = multiprocessing.Pipe()
    g = multiprocessing.Process(target=generate_data, args=(data_end,))
    w = multiprocessing.Process(target=work_on_data, args=(input_end, output_end))
    r = multiprocessing.Process(target=present_results, args=(result_end,))
    g.start()
    w.start()
    r.start()
    g.join()
    w.join()
    r.join()

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
