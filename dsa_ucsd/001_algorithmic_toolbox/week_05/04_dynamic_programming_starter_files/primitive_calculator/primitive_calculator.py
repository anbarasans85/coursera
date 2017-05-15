# Uses python3
import sys

def optimal_sequence(n):
    value = []
    value.insert(0, [0])
    value.insert(1, [1])
    value.insert(2, [1, 2])
    value.insert(3, [1, 3])
    for ni in range(4, n+1):
        value.insert(ni, (sys.maxsize))
        a_list = [] * ni
        v_list = [] * ni
        a_list.append(len(value[ni-1]) + 1)
        v_list.append(value[ni-1])
        if ni % 2 == 0:
            a_list.append(len(value[int(ni/2)]))
            v_list.append(value[int(ni/2)])
        else:
            a_list.append(sys.maxsize)
            v_list.append(sys.maxsize)
        if ni % 3 == 0:
            a_list.append(len(value[int(ni/3)]))
            v_list.append(value[int(ni/3)])
        else:
            a_list.append(sys.maxsize)
            v_list.append(sys.maxsize)
        v1 = list(v_list[a_list.index(min(a_list))])
        v1.append(ni)
        value[ni] = v1
    return value[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
