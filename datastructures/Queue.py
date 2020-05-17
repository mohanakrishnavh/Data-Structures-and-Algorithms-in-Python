
class Queue:

    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, item):
        self.items.insert(0,item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        else:
            print("Queue is empty!")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
