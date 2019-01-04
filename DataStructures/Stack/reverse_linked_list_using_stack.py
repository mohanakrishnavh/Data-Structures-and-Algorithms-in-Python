from Stack import Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    '''
    Reversing a Linked List using Stack
    :param head: Head of the Linked List
    :return: Reversed Linked List
    '''
    current = head
    stack = Stack()
    while current is not None:
        stack.push(current)
        current = current.next

    temp = stack.peek()
    new_head = temp
    stack.pop()
    while stack.is_empty() is False:
        temp.next = stack.peek()
        stack.pop()
        temp = temp.next
    temp.next = None
    return new_head


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next


def main():
    e1 = Node(10)
    e2 = Node(20)
    e3 = Node(30)
    e4 = Node(40)
    e1.next = e2
    e2.next = e3
    e3.next = e4

    head = e1
    print("Linked List before reversal: ")
    print_linked_list(head)
    print()
    print("Linked List after reversal : ")
    new_head = reverse_linked_list(head)
    print_linked_list(new_head)

if __name__ == '__main__':
    main()






