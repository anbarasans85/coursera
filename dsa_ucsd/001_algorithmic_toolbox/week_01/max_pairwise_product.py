# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


def max_pairwise_product(a1):
    result1 = 0
    n1 = len(a1)
    for i in range(0, n1):
        for j in range(i+1, n1):
            if a1[i]*a1[j] > result1:
                result1 = a1[i]*a1[j]
    return result1


def max_pairwise_product_fast(a1):
    n1 = len(a1)
    max_index1 = -1
    for i in range(0, n1):
        if max_index1 == -1 or a[i] > a[max_index1]:
            max_index1 = i
    max_index2 = -1
    for j in range(0, n1):
        if (j != max_index1) and (max_index2 == -1 or a[j] > a[max_index2]):
            max_index2 = j
    return a[max_index1] * a[max_index2]


# result = max_pairwise_product(a)
# print(result)
# result = max_pairwise_product_fast(a)
# print(result)

max_index1 = -1
for i in range(0, len(a)):
    if max_index1 == -1 or a[i] > a[max_index1]:
        max_index1 = i
max_index2 = -1
for j in range(0, len(a)):
    if (j != max_index1) and (max_index2 == -1 or a[j] > a[max_index2]):
        max_index2 = j
if max_index1 != -1 or max_index2 != -1:
    result = a[max_index1] * a[max_index2]
else:
    result = 0

print(result)
