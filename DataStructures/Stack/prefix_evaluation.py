from Stack import Stack


def is_operator(expr):
    '''
    Checks if a given expression is operator
    :param expr: Input expression
    :return: True if the expression is an operator, else False
    '''
    if expr == '+' or expr == '-' or expr == '*' or expr == '/':
        return True
    return False


def is_operand(expr):
    '''
    Checks if a given expression is digit or not
    :param expr: Input expression
    :return: True if the expression is a digit, else False
    '''
    if expr.isdigit():
        return True
    else:
        return False


def perform(operator, op1, op2):
    '''
    Performs arithmetic operation on the given operands
    :param operator: Arithmetic operator
    :param op1: Operand 1
    :param op2: Operand 2
    :return: Result of arithmetic operation on operands
    '''
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2
    else:
        print("Invalid Operation")
        return -1


def evaluate_prefix_expr(prefix_expr):
    '''
    Evaluates a postfix expression using stack
    :param postfix_expr: Postfix expression
    :return: evaluated result
    '''
    stack = Stack()
    n = len(prefix_expr)

    for i in range(n-1, -1, -1):
        if is_operand(prefix_expr[i]):
            stack.push(int(prefix_expr[i]))
        elif is_operator(prefix_expr[i]):
            op1 = stack.peek()
            stack.pop()
            op2 = stack.peek()
            stack.pop()
            result = perform(prefix_expr[i], op1, op2)
            stack.push(result)
    return stack.peek()


def main():
    postfix_expr = "-,+,*,2,3,*,5,4,9"
    postfix_expr = postfix_expr.split(',')
    print(evaluate_prefix_expr(postfix_expr))


if __name__ == '__main__':
    main()
