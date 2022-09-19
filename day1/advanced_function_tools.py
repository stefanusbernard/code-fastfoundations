import random
import sys


def double_number(n):
    return 2 * n


def using_map():
    """Double the given number"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(double_number, random_numbers) = }")


def using_map_and_lambda():
    """Using map with a lambda"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(lambda r: 2 * r, random_numbers) = }")


def using_filter():
    """Filter out words that are in the wrong case"""
    words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban", "sentence", ]
    print(f"{words = }")
    print(f"{filter(lambda w: len(w) > 7, words) = }")

def function_exercise(dict):
    result_dict = dict()
    for key, value in dict.items():
        result_dict[key] = value*value
    return result_dict


test = {'a':1, 'b':2, 'c':3}
def main():
    function_exercise(test)
    # using_map()
    # using_map_and_lambda()
    # using_filter()
    # return 0



if __name__ == '__main__':
    sys.exit(main())
