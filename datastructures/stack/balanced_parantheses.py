def are_pair(opening, closing):
    '''
    Helper function to check if a given parentheses are a pair
    :param opening: opening parentheses
    :param closing: closing parentheses
    :return: True if the pair matches, else False
    '''
    if opening == '(' and closing == ')':
        return True

    elif opening == '{' and closing == '}':
        return True

    elif opening == '[' and closing == ']':
        return True

    return False


def balanced_parentheses(expression):
    '''
    Function to check if the given expression has balanced parentheses
    :param expression: input expression
    :return: True if the parentheses is balances, else False
    '''
    stack = []
    n = len(expression)

    for i in range(n):
        if expression[i] == '(' or expression[i] == '{' or expression[i] == '[':
            stack.append(expression[i])
        elif expression[i] == ')' or expression[i] == '}' or expression[i] == ']':
            if len(stack) == 0 or are_pair(stack[-1], expression[i]) is False:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


def main():
    expression = input("Enter an expression : ")
    if balanced_parentheses(expression):
        print("Balanced")
    else:
        print("Not Balanced")

if __name__ == '__main__':
    main()



