from typing import List


def recursive_binary_search(A: List[int], x: int) -> int:
    """
    Binary Search ( Recursive Implementation)
    :param A: Input Array
    :param x: Element to Search
    :return: Index of the Element

    Time Complexity : O(log n)
    """
    def helper(A, start, end, x):
        mid = start + (end-start)//2

        if start > end:
            return -1

        if x == A[mid]:
            return mid

        elif x < A[mid]:
            return helper(A, 0, mid-1, x)

        elif x > A[mid]:
            return helper(A, mid+1, end, x)

    return helper(A, 0, len(A)-1, x)


A = [2, 6, 13, 21, 36, 47, 63, 81, 97]
x = int(input("Enter the element to search: "))
result = recursive_binary_search(A, x)

if result == -1:
    print("Element not found.")
else:
    print("Element {0} found at index {1}.".format(x, result))