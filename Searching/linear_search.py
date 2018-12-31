def linear_search(A, x):
    '''
    Search for an element in an unsorted array
    :param A: given array
    :return: True if element exists, else False

    Time Complexity : O(n)
    Space Complexity : O(1)
    '''
    for i in range(0, len(A)):
        if A[i] == x:
            return i
    return -1


def main():
    A = [2, 6, 13, 21, 36, 47, 63, 81, 97]
    num = int(input("Enter a number : "))

    result = linear_search(A, num)
    if result == -1:
        print("Number not found in the array.")
    else:
        print("Number {0} found at index {1}.".format(num, result))

if __name__ == '__main__':
    main()
