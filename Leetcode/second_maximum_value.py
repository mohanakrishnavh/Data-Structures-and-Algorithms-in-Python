def second_max_value(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    size = len(arr)

    if size < 2:
        return -1

    max_value, sec_max_value = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
    for i in range(2, size):
        if arr[i] > max_value:
            sec_max_value = max_value
            max_value = arr[i]

        elif arr[i] > sec_max_value:
            sec_max_value = arr[i]

    return sec_max_value


print(second_max_value([9, 2, 3, 6]))
print(second_max_value([4, 2, 1, 5, 0]))
