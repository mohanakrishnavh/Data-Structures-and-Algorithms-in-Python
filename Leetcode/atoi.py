import math


def atoi(input_string):
    """
    :type str: str
    :rtype: int
    """

    MAX_INT = int(math.pow(2, 31) - 1)
    MIN_INT = int(-1 * math.pow(2, 31))

    input_string = input_string.strip()
    size = len(input_string)
    output = ""

    for i in range(size):
        if i == 0 and (input_string[i].isdigit() is True or input_string[i] == '+' or input_string[i] == '-'):
            output += input_string[i]

        elif (i != 0) and input_string[i].isdigit() is True:
            output += input_string[i]
        else:
            break

    if len(output) > 1:
        output = int(output)
        if output > MAX_INT:
            return MAX_INT
        elif output < MIN_INT:
            return MIN_INT
        else:
            return output
    elif output.isdigit() is True:
        return int(output)
    else:
        return 0


'''
inputString = "4193 with words"
print(atoi(inputString))
'''
