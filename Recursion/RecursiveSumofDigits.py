
def recursive_sum_of_digits(n):
    if n < 10:
        return n

    else:
        return (n % 10) + recursive_sum_of_digits(n//10)


num = 4512002
output = recursive_sum_of_digits(num)
print(output)
