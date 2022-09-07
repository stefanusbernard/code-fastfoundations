import random
import sys


def print_5s():
    sssss = "整理、 整頓、 清楚、 清潔、 しつけ"
    print(sssss)
    print(f"{len(sssss) = }")
    sssss_bytes = sssss.encode('utf-8')
    print(f"{len(sssss_bytes) = }")
    print(f"{sssss_bytes = }")


def working_with_bytes():
    b_empty = bytes()
    print(f"{b_empty = }")
    print(f"{len(b_empty) = }")
    b_random = bytes(random.choices(range(256), k=10))
    print(f"{b_random = }")
    b_chars = b'the moon is shining so bright'
    print(f"{b_chars = }")
    # not all byte sequences are encodeable
    s_random = b_random.decode('utf-8')
    # only allows 0..255
    b_fail = bytes([268])  # raises ValueError


def print_triple_quoted():
    string = """
    The Zen of Python, by Tim Peters

    'Beautiful' is better than 'ugly'.
    Explicit is better than implicit.
    "Simple is better than complex".
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    ..."""
    print(string)


def string_search(word, replace_with='fishcake'):
    sentence = "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind."
    # count
    print(f"sentence has {sentence.count(word)} occurrences of '{word}'")
    # find, index
    start_index = sentence.find(word)
    print(f"location of '{word}': {start_index}")
    next_index = sentence.index(word, start_index + len(word))
    print(f"next location of '{word}': {next_index}")
    print(f"{sentence[start_index:start_index + len(word)] = }")
    print(f"{sentence[next_index:next_index + len(word)] = }")
    # replace
    print(f"{sentence.replace(word, replace_with)}")


def string_is_properties(string):
    # isalnum, isalpha, isprintable, isspace
    print(f"{string.isalnum() = }")
    print(f"{string.isalpha() = }")
    print(f"{string.isprintable() = }")
    print(f"{string.isspace() = }")
    # isdecimal, isdigit, isnumeric
    print(f"{string.isdigit() = }")
    print(f"{string.isdigit() = }")
    print(f"{string.isnumeric() = }")
    # isascii, isidentifier
    print(f"{string.isascii() = }")
    print(f"{string.isidentifier() = }")
    # islower, istitle, isupper
    print(f"{string.islower() = }")
    print(f"{string.istitle() = }")
    print(f"{string.isupper() = }")




def main():
    # print_5s()
    # working_with_bytes()
    # print_triple_quoted()
    # string_search('who')
    string_is_properties(input())
    return 0


if __name__ == '__main__':
    sys.exit(main())
