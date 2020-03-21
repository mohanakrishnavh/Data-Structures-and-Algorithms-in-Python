def find_square_sum_of_digits(n):
    """
    Time Complexity: O(k)
    k - Number of digits in n
    """
    total_sum = 0

    while n > 0:
        n, digit = divmod(n, 10)
        total_sum += digit ** 2

    return total_sum


def is_happy(n):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    slow = find_square_sum_of_digits(n)
    fast = find_square_sum_of_digits(find_square_sum_of_digits(n))

    while slow != fast:
        if slow == fast:
            break

        slow = find_square_sum_of_digits(slow)
        fast = find_square_sum_of_digits(find_square_sum_of_digits(fast))

    return fast == 1


print(is_happy(23))
print(is_happy(1))
print(is_happy(12))