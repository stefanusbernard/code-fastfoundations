import multiprocessing
import sys


class GeometricSeries(multiprocessing.Process):
    def __init__(self, a, r, n=10):
        self.a = a
        self.r = r
        self.n = n
        super().__init__()

    def run(self):
        """Where the action is"""
        if self.r == 1:
            print(f"s_{self.n} ({self.a}, {self.r}) = {self.a * (self.n + 1)}")
        else:
            print(f"s_{self.n} ({self.a}, {self.r}) = {self.a * (1 - self.r ** (self.n + 1)) / (1 - self.r)}")

def main():
    geometric_series = GeometricSeries(2, 0.3333333, 100)
    geometric_series.start()
    geometric_series.join()
    return 0


if __name__ == "__main__":
    sys.exit(main())
