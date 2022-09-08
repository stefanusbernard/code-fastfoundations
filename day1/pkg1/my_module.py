"""This module is never going to be called directly so we don't need the import guard"""


def calculate_lucas_numbers(n):
    """Compute the Lucas numbers from """
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n > 2:
        return calculate_lucas_numbers(n - 1) + calculate_lucas_numbers(n - 2)
