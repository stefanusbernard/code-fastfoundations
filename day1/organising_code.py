import sys

import exceptions


def main():
    print(
        f"""{exceptions.calculate_geometric_series(int(input("a: ")), float(input("r: ")), int(input("n: "))) = }"""
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
