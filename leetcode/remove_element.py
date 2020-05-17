def remove_element(arr, key):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)

    i = 0
    for j in range(0, n):
        if arr[j] != key:
            arr[i] = arr[j]
            i += 1

    return i


print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
