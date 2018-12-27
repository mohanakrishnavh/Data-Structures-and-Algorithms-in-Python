'''
Selction Sort

Time Complexity : O(n^2)
Best Case : O(n)
Average Case : O(n^2)
Worst Case : O(n^2)

Space Complexity : O(1)
'''


def bubble_sort(A):
    n = len(A)
    for k in range(1, n):
        flag = 0
        for i in range(0, n-k):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = 1

        if flag == 0:
            break
    return A

A = [2, 7, 4, 1, 5, 3]
print(bubble_sort(A))
