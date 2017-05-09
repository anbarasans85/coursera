# Uses python3
import sys


def get_change(m):
    count = 0
    change_list = [10, 5, 1]
    for c in change_list:
        while m - c >= 0:
            m -= c
            count += 1
    return count


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
