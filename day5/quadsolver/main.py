"""
Main functions
--------------

This module has two functions, which can be called as follows.

>>> solve_quadratic(1, 2, 1)
>>> main()


"""
import sys
import cmath



def solve_quadratic(a, b, c):
    """Solve quadratic equation

    :param float a: coefficient of $x^$
    :param float b: coefficient of $x$
    :param float c: constant
    :return tuple(x1, x2): complex solutions
    :rtype: complex
    """
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + cmath.sqrt(discriminant)) / 2 * a
    x2 = (-b + cmath.sqrt(discriminant)) / 2 * a
    return x1, x2


def main():
    """Main entry point

    :return 0: exit OK
    :rtype: int
    """
    print(f"{solve_quadratic(1, 2, 1) = }")
    return 0


if __name__ == "__main__":
    sys.exit(main())
