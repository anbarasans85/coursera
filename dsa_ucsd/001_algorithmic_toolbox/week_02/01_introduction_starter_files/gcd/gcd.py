# Uses python3
import sys


def gcd_naive(a, b):
    if b == 0:
        return a
    return gcd_naive(b, (a % b))


if __name__ == "__main__":
    inputn = sys.stdin.read()
    ai, bi = map(int, inputn.split())
    print(gcd_naive(ai, bi))
