# Uses python3
import sys

def get_majority_element(a, left, right):
    count_dict = dict()
    count_dict = count_dict.fromkeys(a, 0)
    for e in a:
        count_dict[e]+= 1
    for k,v in count_dict.items():
        if v > (len(a)/2):
            return 1
    return -1
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
