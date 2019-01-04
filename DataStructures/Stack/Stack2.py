class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        '''
        Push an element x into the stack
        :param x: input element
        '''
        current = Node(x)
        if self.head is None:
            self.head = current
        else:
            current.next = self.head
            self.head = current
        self.size += 1

    def pop(self):
        '''
        Removes the topmost element from the stack
        '''
        if self.head is None:
            print("Stack is empty")
        else:
            current = self.head
            new_head = current.next
            self.head = new_head
            self.size -= 1

    def is_empty(self):
        '''
        Checks if the stack is empty
        :return: returns True if stack is empty, else False
        '''
        if self.head is None:
            return True
        else:
            return False

    def peek(self):
        '''
        Returns the topmost element from the stack
        '''
        if self.head is None:
            print("Stack is empty.")
        else:
            current = self.head
            return current.data

    def get_size(self):
        '''
        Returns the size of the stack
        '''
        return self.size


def main():
    s = Stack()
    s.push(2)
    s.push(10)
    print(s.get_size())
    print(s.peek())
    s.pop()
    s.pop()
    print(s.is_empty())
    s.pop()


if __name__ == '__main__':
    main()








