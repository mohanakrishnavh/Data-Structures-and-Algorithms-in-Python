
def recursive_string_reversal(s, output=None):
    # Base Case
    if len(s) <= 1:
        return s

    # recursion
    else:
        if output is None:
            output = ""
            output += s[-1]
        else:
            output += s[-1]
        return output + recursive_string_reversal(s[0:len(s)-1])

    return output

str1 = "Hello World"
output = recursive_string_reversal(str1)
print(output)

'''
def reverse(s):
    # Base Case
    if len(s) <= 1:
        return s

    # recursion
    return reverse(s[1:]) + s[0]

'''
