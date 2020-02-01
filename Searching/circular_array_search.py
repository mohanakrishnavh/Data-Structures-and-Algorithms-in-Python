from typing import List


def circular_array_search(A: List[int], x) -> int:
    """
    Searches for a given element in circular sorted array
    :param A: Input Array
    :param x: Element to Search
    :return: Index of the Element
    """
    start = 0
    end = len(A)-1

    while start <= end:
        mid = start + (end-start)//2

        # Case 1: If mid element is the element we are searching
        if A[mid] == x:
            return mid

        # Case 2: Searching in the right half
        if A[mid] <= A[end]:
            # If we are in sorted half
            if A[mid] <= x <= A[end]:
                start = mid+1
            # If we are in unsorted half
            else:
                end = mid-1

        # Case 3: Searching in the left half
        if A[start] <= A[mid]:
            # If we are in sorted half
            if A[start] <= x <= A[mid]:
                end = mid-1
            # If we are in unsorted half
            else:
                start = mid+1

    return -1


A = [12, 14, 18, 21, 3, 6, 8, 9]
x = int(input("Enter the number to search: "))
result = circular_array_search(A, x)

if result != -1:
    print("Number {0} found at index: {1}".format(x, result))
else:
    print("Number not found")
