from datastructures.linkedlist.LinkedList import LinkedList, Node


def reverse_linked_list(head: Node) -> Node:
    previous_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    head = previous_node
    return head


linked_list = LinkedList()
reversed_head = reverse_linked_list(linked_list.head)
linked_list.print_list(reversed_head)

linked_list2 = LinkedList()
linked_list2.insert(10)
reversed_head2 = reverse_linked_list(linked_list2.head)
linked_list2.print_list(reversed_head2)

linked_list3 = LinkedList()
linked_list3.insert(10)
linked_list3.insert(20)
linked_list3.insert(30)
linked_list3.insert(40)
reversed_head3 = reverse_linked_list(linked_list3.head)
linked_list3.print_list(reversed_head3)




