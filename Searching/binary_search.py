def binary_search(A, x):
    '''
    Search for an element in a sorted array
    :param A: given array
    :param x : search element
    :return: True if element exists, else False

    Time Complexity : O(log n)
    Space Complexity : O(1)
    '''
    # return binary_search_util(A, 0, len(A), x)
    return binary_search_util_recursive(A, 0, len(A)-1, x)


def binary_search_util(A, low, high, x):
    '''

    :param A: given array
    :param low: lowest index of search space
    :param high: highest index of search space
    :param x: search element
    :return: True if element is found, else False
    '''
    start = low
    end = high-1
    while start <= end:
        mid = (start + end)//2
        if A[mid] == x:
            return mid
        elif x < A[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_search_util_recursive(A, start, end, x):
    '''

    :param A: given array
    :param low: lowest index of search space
    :param high: highest index of search space
    :param x: search element
    :return: True if element is found, else False
    '''
    if start > end:
        return -1

    mid = start + (end - start)//2
    if A[mid] == x:
        return mid

    elif A[mid] < x:
        return binary_search_util_recursive(A, mid+1, end, x)

    else:
        return binary_search_util_recursive(A, start, mid-1, x)


def main():
    A = [2, 6, 13, 21, 36, 47, 63, 81, 97]
    num = int(input("Enter a number : "))

    result = binary_search(A, num)
    if result == -1:
        print("Number not found in the array.")
    else:
        print("Number {0} found at index {1}.".format(num, result))

if __name__ == '__main__':
    main()
