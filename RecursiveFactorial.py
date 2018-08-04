
def recursive_factorial(n):

    # base case
    if n == 0 or n == 1:
        return 1

    else:
        return n * recursive_factorial(n-1)


n = 5
output = recursive_factorial(5)
print(output)

