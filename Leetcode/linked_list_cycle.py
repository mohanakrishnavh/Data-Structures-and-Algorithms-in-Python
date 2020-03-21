from DataStructures.LinkedList.LinkedList import Node, LinkedList
from typing import Union


def has_cycle(head: Node) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False


def calculate_cycle_length(slow: Node) -> int:
    """
    Helper function to calculate length of the cycle

    Time Complexity: O(n)
    """
    length = 0
    current_node = slow

    while True:
        current_node = current_node.next
        length += 1

        if current_node == slow:
            break

    return length


def cycle_length(head: Node) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if head is None or head.next is None:
        return 0

    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        if slow == fast:
            break

        slow = slow.next
        fast = fast.next.next

    length = calculate_cycle_length(slow) if has_cycle(head) else 0

    return length


def find_cycle_start(head: Node) -> Union[Node, None]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    ptr_1 = head
    ptr_2 = head

    cycle_size = cycle_length(head)

    # If there is no cycle
    if cycle_size == 0:
        return None

    # Move pointer 2 by cycle_size nodes
    while cycle_size > 0:
        ptr_2 = ptr_2.next
        cycle_size -= 1

    while ptr_1 != ptr_2:
        ptr_1 = ptr_1.next
        ptr_2 = ptr_2.next

    return ptr_1


list_1 = Node(1)
list_1.next = Node(2)
list_1.next.next = Node(3)
list_1.next.next.next = Node(4)
list_1.next.next.next.next = Node(5)
list_1.next.next.next.next.next = Node(6)
list_1.next.next.next.next.next.next = list_1.next.next

list_2 = LinkedList()
list_2.insert(1)
list_2.insert(2)
list_2.insert(3)
list_2.insert(4)
list_2.insert(5)
list_2.insert(6)

list_3 = Node(1)
list_3.next = Node(2)
list_3.next.next = Node(3)
list_3.next.next.next = Node(4)
list_3.next.next.next.next = Node(5)
list_3.next.next.next.next.next = Node(6)
list_3.next.next.next.next.next.next = list_3.next.next.next

print(has_cycle(list_1))
print(has_cycle(list_2.get_head()))
print(cycle_length(list_1))

print(find_cycle_start(list_1).data)
print(find_cycle_start(list_2.get_head()))
print(find_cycle_start(list_3).data)
