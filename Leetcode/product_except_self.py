def product_except_self(arr):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    result = []
    for i, x in enumerate(arr):
        product = 1
        for j, y in enumerate(arr):
            if i != j:
                product *= y
        result.append(product)

    return result


def product_except_self_2(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = []
    size = len(arr)

    left = 1
    for i in range(0, size):
        result.append(left)
        left = left * arr[i]

    right = 1
    for i in range(size-1, -1, -1):
        result[i] = result[i] * right
        right = right * arr[i]

    return result


print(product_except_self([1, 2, 3, 4]))
print(product_except_self_2([1, 2, 3, 4]))
