'''
Insertion Sort

Time Complexity : O(n^2)
Best Case : O(n)
Average Case : O(n^2)
Worst Case : O(n^2)

Space Complexity : O(1)
'''


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        value = A[i]
        hole = i
        while hole > 0 and A[hole - 1] > value:
            A[hole] = A[hole - 1]
            hole -= 1
        A[hole] = value
    return A

A = [2, 7, 4, 1, 5, 3]
print(insertion_sort(A))
