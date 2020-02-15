from DataStructures.LinkedList.LinkedList import LinkedList
from DataStructures.LinkedList.LinkedList import Node


def add_two_numbers(l1: Node, l2: Node) -> Node:
    head = None
    current_node = None
    carry = 0

    while (l1 is not None) or (l2 is not None) or (carry > 0):
        total = carry

        # case 1: When we have both nodes
        if (l1 is not None) and (l2 is not None):
            total += (l1.data + l2.data)
            l1 = l1.next
            l2 = l2.next

        # case 2: When one of the nodes is None
        elif l1 is None:
            total += l2.data
            l2 = l2.next

        elif l2 is None:
            total += l1.data
            l1 = l1.next

        # Calculating value of the node and carry
        val = total % 10
        carry = total // 10
        new_node = Node(val)

        # If it is the first node, save it as head
        if head is None:
            head = current_node = new_node
        else:
            current_node.next = new_node
            current_node = new_node

    return head


l1 = LinkedList()
l1.insert(2)
l1.insert(4)
l1.insert(3)

l2 = LinkedList()
l2.insert(5)
l2.insert(6)
l2.insert(4)

head = add_two_numbers(l1.head, l2.head)
l3 = LinkedList()
l3.print_list(head)
