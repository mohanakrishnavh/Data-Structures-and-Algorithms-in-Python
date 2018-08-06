
def linear_search(arr, x):
    for idx, element in enumerate(arr):
        if element == x:
            return idx
    return -1


nums = [10, 20, 5, 6, 3, 2, 1]
result = linear_search(nums, 5)
print(result)
