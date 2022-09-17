import argparse


def parse_args():
    """Parse command line arguments

    :return args: arguments as an `args.Namespace` object
    :rtype args: args.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('coefficients', type=float, nargs=3, help="coefficients for a, b, and c (in order)")
    args = parser.parse_args()
    return args
