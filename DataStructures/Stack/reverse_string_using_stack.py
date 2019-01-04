from Stack import Stack


def reverse_string(S):
    '''
    Reverse a String using Stack
    :param S: Input String
    :return: Reversed String

    Time Complexity : O(n)
    Space Complexity : O(n)
    '''
    stack = Stack()
    S = list(S)
    n = len(S)
    # Pushing all characters into the stack
    for i in range(n):
        stack.push(S[i])

    # Popping the characters in  reverse order
    i = 0
    while stack.is_empty() is False:
        S[i] = stack.peek()
        stack.pop()
        i += 1

    return "".join(S)


def main():
    S = "mohanakrishnavh"
    print(reverse_string(S))


if __name__ == '__main__':
    main()
