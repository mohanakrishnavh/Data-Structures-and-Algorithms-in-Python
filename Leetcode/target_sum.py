def target_sum(arr, target):
    n = len(arr)
    left = 0
    right = n-1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [arr[left], arr[right]]

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return [None, None]


print(target_sum([1, 2, 3, 4, 6], 6))
print(target_sum([1, 2, 3, 8, 8, 8, 8], 10))
