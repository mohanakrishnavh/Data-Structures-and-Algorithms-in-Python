
class Deque:

    def __init__(self):
        self.items = []
        self.size = 0

    def append(self, item):
        self.items.append(item)
        self.size += 1

    def append_left(self, item):
        self.items.insert(0, item)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        else:
            print("Deque is empty!")

    def pop_left(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop(0)
        else:
            print("Deque is empty!")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
