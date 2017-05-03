# Uses python3
import sys


def calc_fib(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def pisano_period_length(pm):
    length = 2
    fibp = 1
    previous = 1
    current = 1
    while 1:
        previous, current = current, previous + current
        fib1 = current % pm
        if fibp == 0 and fib1 == 1:
            return length
        fibp = fib1
        length += 1


def get_fibonacci_huge(n, m):
    reminder = n % pisano_period_length(m)
    return calc_fib(reminder) % m


if __name__ == '__main__':
    inputn = sys.stdin.read()
    ni, mi = map(int, inputn.split())
    print(get_fibonacci_huge(ni, mi))
