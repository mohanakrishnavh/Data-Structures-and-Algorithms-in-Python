def sorted_squares(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)

    i = 0
    while arr[i] < 0:
        i += 1

    pos_ptr = i
    neg_ptr = i-1
    result = []

    while 0 <= neg_ptr or pos_ptr < n:
        neg_idx_val = abs(arr[neg_ptr]) if neg_ptr >= 0 else float('inf')
        pos_idx_val = arr[pos_ptr] if pos_ptr < n else float('inf')

        if pos_idx_val < neg_idx_val:
            x = pos_idx_val
            pos_ptr += 1
        else:
            x = neg_idx_val
            neg_ptr -= 1

        result.append(x*x)

    return result


print(sorted_squares([-4, -1, 0, 3, 10]))
