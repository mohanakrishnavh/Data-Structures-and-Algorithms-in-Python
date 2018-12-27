'''
Selction Sort

Time Complexity : O(n^2)
Space Complexity : O(1)
'''


def selection_sort(A):
    n = len(A)
    for i in range(0, n-1):
        i_min = i
        for j in range(i+1, n):
            if A[j] < A[i_min]:
                i_min = j

        A[i], A[i_min] = A[i_min], A[i]
    return A

A = [2, 7, 4, 1, 5, 3]
print(selection_sort(A))
