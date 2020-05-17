class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, x):
        '''
        Push an element x into the stack
        :param x: input element
        '''
        self.top += 1
        self.stack.append(x)

    def pop(self):
        '''
        Removes the topmost element from the stack
        '''
        if self.top > -1:
            self.top -= 1
            self.stack.pop()
        else:
            print("stack is empty.")

    def peek(self):
        '''
        Returns the topmost element from the stack
        '''
        if self.top > -1:
            return self.stack[self.top]
        else:
            print("stack is empty.")

    def is_empty(self):
        '''
        Checks if the stack is empty
        :return: returns True if stack is empty, else False
        '''
        return self.top == -1

    def get_size(self):
        '''
        Returns the size of the stack
        '''
        return self.top+1


def main():
    s = Stack()
    s.push(2)
    s.push(10)
    print(s.get_size())
    print(s.peek())
    s.pop()
    print(s.is_empty())
    s.push(7)
    s.push(5)
    print(s.peek())
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print(s.peek())

if __name__ == '__main__':
    main()




