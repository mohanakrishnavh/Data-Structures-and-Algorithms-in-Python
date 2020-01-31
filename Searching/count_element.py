from typing import List


def find_min_index(A: List[int], x: int) -> int:
    """
    Finds the max index of the element being searched
    :param A: Input Array
    :param x: Element to search in the array
    :return:
    """
    min_index = -1
    start = 0
    end = len(A)-1

    while start <= end:
        mid = start + (end-start)//2

        if A[mid] == x:
            min_index = mid
            end = mid - 1
        elif x < A[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return min_index


def find_max_index(A: List[int], x: int) -> int:
    """
    Finds the max index of the element being searched
    :param A: Input Array
    :param x: Element to search in the array
    :return:
    """
    max_index = -1
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if A[mid] == x:
            max_index = mid
            start = mid + 1
        elif x < A[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return max_index


def count_element(A: List[int], x: int) -> int:
    """
    Counts the number of occurrence of an element in the given sorted array
    :param A: Input Array
    :param x: Element to search in the array
    :return: Count of the element being searched

    Time Complexity: O(log n)
    """
    min_index = find_min_index(A, x)
    max_index = find_max_index(A, x)

    return (max_index-min_index)+1


A = [1, 1, 3, 3, 5, 5, 5, 5, 9, 11]
x = int(input("Enter the element:"))
result = count_element(A, x)
print("Count of the element: ", result)