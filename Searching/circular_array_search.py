def circular_array_search(A, x):
    '''
    Search for an element in sorted circular array
    :param A: given array
    :param x: search element
    :return: index of the element found in the array
    '''
    n = len(A)
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end)//2

        # case 1:
        if A[mid] == x:
            return mid

        # case 2:
        if A[mid] <= A[end]:
            if A[mid] < x <= A[end]:
                start = mid + 1
            else:
                end = mid - 1

        # case 3:
        if A[start] <= A[mid]:
            if A[start] <= x < A[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


def main():
    A = [12, 14, 18, 21, 3, 6, 8, 9]
    num = int(input("Enter the number : "))
    print("Element {0} found at index {1}.".format(num, circular_array_search(A, num)))

if __name__ == '__main__':
    main()
