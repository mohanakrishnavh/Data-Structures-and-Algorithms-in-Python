from typing import List


def binary_search(A: List[int], x: int) -> int:
    """
    Binary Search
    :param A: Input Array
    :param x: Element to Search
    :return: Index of the Element

    Time Complexity : O(log n)
    """
    start = 0
    end = len(A)-1

    while start <= end:
        # (start + end) might overflow
        mid = start + (end-start)//2

        # If we find the element return its index
        if mid == x:
            return mid

        # If the element is smaller than the middle element, search in the left half of the array
        if x < A[mid]:
            end = start-1

        # If the element is greater than the middle element, search in the right half of the array
        else:
            start = mid+1

    # If the element is not found
    return -1


A = [2, 6, 13, 21, 36, 47, 63, 81, 97]
x = int(input("Enter the number to search: "))
result = binary_search(A, x)

if result == -1:
    print("Element not found.")
else:
    print("Element {0} found at index {1}.".format(x, result))
