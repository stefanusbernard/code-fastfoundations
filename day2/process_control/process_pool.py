import os, sys
import multiprocessing
import cmath
import random
import time


def solve_quadratic(eq):
   a, b, c = eq
   if a == 0 and b != 0 and c != 0:
       return 0, -c / b
   elif a == 0 and b == 0:
       return None, None
   elif a == 0 and c == 0:
       return 0, 0
   discriminant = b ** 2 - 4 * a * c
   x1 = (-b + cmath.sqrt(discriminant)) / 2 / a
   x2 = (-b - cmath.sqrt(discriminant)) / 2 / a
   time.sleep(0.000001)  # 1 µs delay to simulate a more demanding task
   return x1, x2


def main():
   equations = [(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)) for _ in range(2000000)]
   start = time.time()
   solutions = list(map(solve_quadratic, equations))
   print(f"Calculated in {time.time() - start:.10f} seconds")
   start = time.time()
   with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
       solutions = pool.map(solve_quadratic, equations)
   print(f"Calculated in {time.time() - start:.10f} seconds")
   procs = list()
   for i in range(10):
       proc = multiprocessing.Process(target=solve_quadratic, )
       procs.append(proc)
   return os.EX_OK


if __name__ == '__main__':
   sys.exit(main())
