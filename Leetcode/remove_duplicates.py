def remove_duplicates(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)

    if n == 0:
        return -1

    i = 0
    for j in range(1, n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i+1


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
