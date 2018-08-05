
def merge(left_arr, right_arr):
    result = [] # sorted result array
    i, j = 0, 0

    # compare and append to the sorted list until one of the arrays get exhausted
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    # add any remaining element to the list
    result += left_arr[i:]
    result += right_arr[j:]
    return result


def merge_sort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr

    mid = int(len(arr)/2)
    left_array = merge_sort(arr[:mid])
    right_array = merge_sort(arr[mid:])

    return merge(left_array, right_array)

arr = [11, 2, 5, 4, 56, 2, 12, 23]
result = merge_sort(arr)
print(result)
