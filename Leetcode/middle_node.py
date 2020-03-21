from typing import Union
from DataStructures.LinkedList.LinkedList import LinkedList, Node


def get_middle_node(head: Node) -> Union[Node, None]:
    """
    Time Complexity: O(n)
    """
    if head is None or head.next is None:
        return None

    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


list_1 = LinkedList()
list_1.insert(1)
list_1.insert(2)
list_1.insert(3)
list_1.insert(4)
list_1.insert(5)
print(get_middle_node(list_1.get_head()).data)
