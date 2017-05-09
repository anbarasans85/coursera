# Uses python3
import sys


def get_optimal_value(capacity_, weights_, values_):
    value = 0.
    unit_value_list = list()
    for i in range(len(weights_)):
        unit_value_list.append([values_[i]/weights[i], weights[i], values_[i]])
    unit_value_list = sorted(unit_value_list, key=lambda x: x[0], reverse=True)
    for e in unit_value_list:
        while capacity_ > 0 and e[1] > 0:
            value += e[0]
            capacity_ -= 1
            e[1] -= 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
