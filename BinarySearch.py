
def binary_search(arr, left, right, x):
    # Base Case
    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == x:
            return mid

        # Check in the left sub-array
        elif arr[mid] < x:
            left = mid + 1

        # Check in the right sub-array
        else:
            right = mid - 1

    # Element is not present in the array
    return -1

arr = [2, 3, 4, 10, 40]
size = len(arr)-1
x = 4
result = binary_search(arr, 0, size, x)
print(result)
