def rearrange(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    left = []
    right = []
    zeros = []

    for x in arr:
        if x < 0:
            left.append(x)
        elif x > 0:
            right.append(x)
        else:
            zeros.append(x)

    return left + zeros + right


def rearrange_pythonic(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    return [i for i in arr if i < 0] + [i for i in arr if i == 0] + [i for i in arr if i > 0]


def rearrange_inplace(arr):
    left_most_pos_idx = 0
    size = len(arr)

    for i in range(size):
        if arr[i] < 0:
            if i is not left_most_pos_idx:
                arr[i], arr[left_most_pos_idx] = arr[left_most_pos_idx], arr[i]
            left_most_pos_idx += 1

    return arr


print(rearrange([10, -1, 20, 4, 0, 5, -9, -6]))
print(rearrange_pythonic([10, -1, 20, 4, 0, 5, -9, -6]))
print(rearrange_inplace([10, -1, 20, 4, 5, -9, -6]))
