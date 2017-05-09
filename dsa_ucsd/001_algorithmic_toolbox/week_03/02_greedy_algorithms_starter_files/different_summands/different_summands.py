# Uses python3
import sys


def optimal_summands(ni):
    summands_ = list()
    i = 1
    summands_.append(i)
    ni -= i
    while ni > 0:
        i += 1
        r = ni - i
        if i not in summands_ and r not in summands_:
            summands_.append(i)
            ni -= i
        else:
            summands_.append(ni)
            break
    return summands_

if __name__ == '__main__':
    input_ = sys.stdin.read()
    n = int(input_)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
