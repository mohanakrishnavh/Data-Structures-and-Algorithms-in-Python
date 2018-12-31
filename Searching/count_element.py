def count_element_occurrence(A, x):
    '''
    Function to count the occurrences of a given element in a sorted array
    :param A: given array
    :param x: element to search and count
    :return: count of the element x in the array

    Time Complexity : O(log n) [Worst Case : O(n), when all elements are same]
    '''
    n = len(A)-1
    if A[0] == A[n]:
        return n+1

    min_index = find_min_index(A, 0, n, x)
    max_index = find_max_index(A, 0, n, x)
    if min_index == max_index == -1:
        return 0
    return (max_index - min_index) + 1


def find_min_index(A, start, end, x):
    '''
    Find the min index of an element in sorted array
    :param A: given array
    :param start: start index
    :param end: end index
    :param x: search element
    :return: minimum index of a search element
    '''
    result = -1
    while start <= end:
        mid = (start+end)//2
        if A[mid] == x:
            result = mid
            end = mid - 1

        elif x < A[mid]:
            end = mid - 1

        else:
            start = mid + 1
    return result


def find_max_index(A, start, end, x):
    '''
    Find the max index of an element in sorted array
    :param A: given array
    :param start: start index
    :param end: end index
    :param x: search element
    :return: maximum index of a search element
        '''
    result = -1
    while start <= end:
        mid = (start+end)//2
        if A[mid] == x:
            result = mid
            start = mid + 1

        elif x < A[mid]:
            end = mid - 1

        else:
            start = mid + 1
    return result


def main():
    # A = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
    A = [1, 1, 1, 1, 1, 1, 1, 1]
    num = int(input("Enter the number : "))
    print("Number {0} occurs {1} times.".format(num, count_element_occurrence(A, num)))

if __name__ == '__main__':
    main()
