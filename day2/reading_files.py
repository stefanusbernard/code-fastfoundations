import sys


def opening_and_closing_files():
    f = open("macintosh.txt")  # details: https://docs.python.org/3/library/functions.html#open
    quote = f.read()
    print(f"{quote = }")
    # try and read again
    quote_again = f.read()
    print(f"{quote_again = }")
    # don't forget!
    f.close()


def reading_file_contents():
    with open("macintosh.txt") as f:
        # read everything
        print(f"{f.read()[:30]}...")

    print(f"{f = }")
    print(f"{f.closed = }")
    # print(f"{f.read() = }") # raises ValueError: I/O operation on closed file

    with open("macintosh.txt") as f:
        # read one line at a time; up to the \n
        print(f"{ f.readline() = }")

    with open("macintosh.txt") as f:
        # list of all lines
        print(f"{ f.readlines() = }")


def iterating_over_file_contents():
    with open("macintosh.txt") as f:
        for row in f:
            print(row)


def navigating_files():
    with open("butterfly.txt") as f:
        # first let's read everything
        print(f"{f.read() = }")
        # try and read again... nothing
        print(f"{f.read() = }")
        # where are we?
        print(f"{f.tell() = }")
        # let's go back to the beginning
        print(f"{f.seek(0) = }")
        # ten steps forward....
        print(f"{f.seek(10) = }")
        # perfect!
        print(f"{f.read() = }")


def main():
    # opening_and_closing_files()
    # reading_file_contents()
    # iterating_over_file_contents()
    navigating_files()
    return 0


if __name__ == '__main__':
    sys.exit(main())
