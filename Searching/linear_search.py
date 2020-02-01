from typing import List


def linear_search(A: List[int], x: int) -> int:
    """
    Linear Search
    :param A: Input Array
    :param x: Element to Search
    :return: Index of the Element

    Time Complexity : O(n)
    """
    n = len(A)

    for i in range(n):
        if A[i] == x:
            return i

    return -1


A = [2, 6, 13, 21, 36, 47, 63, 81, 97]
x = int(input("Enter the number to search: "))
result = linear_search(A, x)

if result == -1:
    print("Number not found.")
else:
    print("Number {0} found at index {1}.".format(x, result))
