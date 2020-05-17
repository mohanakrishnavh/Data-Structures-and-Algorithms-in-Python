import math


def find_minimum(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    min_value = math.inf

    for x in arr:
        if x < min_value:
            min_value = x

    return min_value


print(find_minimum([10, 2, 5, 6, 8]))
