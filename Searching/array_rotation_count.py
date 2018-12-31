def array_rotation_count(A):
    '''
    Return the rotation count of the circular array
    :param A: given array
    :return: array rotation count
    '''
    n = len(A)
    start = 0
    end = n-1

    while start <= end:
        # case 1
        if A[start] <= A[end]:
            return start

        mid = (start+end)//2
        next = (mid+1) % n
        prev = (mid+n-1) % n

        # case 2
        if A[prev] <= A[mid] <= A[next]:
            return mid

        # case 3
        if A[mid] <= A[end]:
            end = mid-1

        # case 4
        if A[mid] >= A[start]:
            start = mid+1
    return -1


def main():
    A = [11, 12, 15, 18, 2, 5, 6, 8]
    # B = [1, 2, 3, 4, 5, 6]
    print("Array is rotated {0} times.".format(array_rotation_count(A)))

if __name__ == '__main__':
    main()
