from typing import List


def array_rotation_count(A: List[int]) -> int:
    """
    Return the rotation count of the circular array
    :param A: given array
    :return: array rotation count

    Time Complexity : O(log n)
    """
    start = 0
    end = len(A)-1
    n = len(A)

    while start <= end:
        # Case 1 : If we are in sorted half of the array
        if A[start] <= A[end]:
            return start

        mid = start + (end-start)//2
        next = (mid+1) % n
        prev = (mid+n-1) % n

        # Case 2: If we are at the pivot element - elements on both sides are greater
        if A[prev] >= A[mid] <= A[next]:
            return mid

        # Case 3: If we are in unsorted half, middle element is smaller than element at the end
        if A[mid] <= A[end]:
            end = mid - 1

        # Case 4: If we are in unsorted half, middle element is greater than element at the end
        if A[mid] >= A[start]:
            start = mid + 1


A = [11, 12, 15, 18, 2, 5, 6, 8]
print("Array rotation count: ", array_rotation_count(A))
