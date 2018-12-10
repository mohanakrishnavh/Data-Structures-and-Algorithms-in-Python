
class Stack:

    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()

        else:
            print("Stack is empty!")

    def peek(self):
        if self.size > 0:
            return self.items[-1]
        else:
            print("Stack is empty!")

    def get_size(self):
        return self.size
