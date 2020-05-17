from datastructures.linkedlist.LinkedList import Node, LinkedList


def remove_duplicates(head: Node):
    if head is None:
        return

    nodeMap = {}
    uniqueList = LinkedList()

    current_node = head
    while current_node is not None:
        if current_node.data not in nodeMap:
            uniqueList.insert(current_node.data)
            nodeMap[current_node.data] = 1

        current_node = current_node.next

    return uniqueList


list1 = LinkedList()
list1.insert(10)
list1.insert(20)
list1.insert(20)
list1.insert(20)
list1.insert(10)
list1.insert(30)
list1.insert(40)
list1.insert(50)
resultList = remove_duplicates(list1.get_head())
resultList.print_list()