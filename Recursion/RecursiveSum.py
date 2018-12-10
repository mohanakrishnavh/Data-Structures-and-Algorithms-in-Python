
def recursive_sum(n):

    # base case
    if n == 0:
        return 0

    else:
        return n + recursive_sum(n-1)


n = 4
output = recursive_sum(4)
print(output)

