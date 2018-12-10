
class Node:
    def __init__(self, value):
        self.element = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def append_left(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def remove(self):
        if self.size > 0:
            current = self.head
            previous = None
            if self.head == self.tail:
                self.head = self.tail = None
                self.size -= 1
            else:
                while current.next is not None:
                    previous = current
                    current = current.next
                previous.next = None
                self.tail = previous
                self.size -= 1
        else:
            print("List is empty.")

    def remove_left(self):
        if self.size > 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
        else:
            print("List is empty.")

    def remove_value(self, value):
        if self.size > 0:
            current = self.head
            previous = None
            while current is not None:
                if current.element == value:
                    # case to check if it is not the head node
                    if previous is not None:
                        previous.next = current.next
                        if current.next is None:
                            self.tail = previous
                    else:
                        self.head = current.next
                previous = current
                current = current.next
            self.size -= 1
        else:
            print("List is empty.")

    def find(self, value):
        index = 0
        if self.size > 0:
            current = self.head
            while current is not None:
                if current.element == value:
                    return index
                current = current.next
                index += 1
            print("Element not found in the list.")
            return None
        else:
            print("List is empty.")

    def show(self):
        if self.size > 0:
            current = self.head
            while current is not None:
                if current == self.tail:
                    print(current.element)
                else:
                    print("{0} -> ".format(current.element), end=" ")
                current = current.next
        else:
            print("List is empty.")

    def get_size(self):
        return self.size
