from collections import OrderedDict


def first_non_repeating_integer(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(m)
    """
    count_map = OrderedDict()

    for x in arr:
        if x in count_map:
            count_map[x] = count_map[x]+1
        else:
            count_map[x] = 1

    for key, value in count_map.items():
        if count_map[key] == 1:
            return key

    return -1


print(first_non_repeating_integer([9, 2, 3, 2, 6, 6]))
print(first_non_repeating_integer([4, 5, 1, 2, 0, 4]))
