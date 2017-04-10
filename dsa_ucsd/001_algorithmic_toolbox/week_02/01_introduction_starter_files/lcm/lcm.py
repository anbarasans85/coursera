# Uses python3
import sys


def gcd_naive(a, b):
    if b == 0:
        return a
    return gcd_naive(b, (a % b))


def lcm_naive(a, b):
    return (a * b) // gcd_naive(a, b)


if __name__ == '__main__':
    inputn = sys.stdin.read()
    ai, bi = map(int, inputn.split())
    print(lcm_naive(ai, bi))
