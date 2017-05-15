# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    val = list(w)
    value = [[0 for x in range(len(w)+1)] for x in range(W+1)]
    for ni in range(1, n+1):
        for wi in range(1, W+1):
            value[wi][ni] = value[wi][ni-1]
            if w[ni-1] <= wi:
                v1 = value[wi-w[ni-1]][ni-1] + val[ni-1]
                if value[wi][ni] < v1:
                    value[wi][ni] = v1
 
    return value[W][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
