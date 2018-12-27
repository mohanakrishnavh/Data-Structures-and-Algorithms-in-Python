import random


def partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A):
    quick_sort_2(A, 0, len(A)-1)
    return A


def quick_sort_2(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort_2(A, p, q-1)
        quick_sort_2(A, q+1, r)


arr = [11, 2, 5, 4, 56, 2, 12, 23]
quick_sort(arr)
print(arr)
