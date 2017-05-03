# Uses python3
import sys

def fibonacci(n):
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


def fibonacci_sum_naive(n):
    pperiod = pisano_period_length(10)
    reminder = n % pperiod
    print(fibonacci(reminder + 2) - 1)
    return (fibonacci(reminder + 2) - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
