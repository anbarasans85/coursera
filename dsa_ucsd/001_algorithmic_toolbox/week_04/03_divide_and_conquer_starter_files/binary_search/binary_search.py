# Uses python3
import sys

def binary_search(input_a, input_x):
    low, high = 0, (len(input_a) - 1)
    # write your code here)
    while low <= high:
        mid = int((low  + high)/2)
        if input_a[mid] == input_x:
            return mid
        elif input_a[mid] < input_x:
            low = mid + 1
        elif input_a[mid] > input_x:
            high = mid - 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
