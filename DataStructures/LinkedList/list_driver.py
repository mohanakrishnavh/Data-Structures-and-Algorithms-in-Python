from DataStructures.LinkedList.LinkedList import LinkedList

linked_list = LinkedList()
linked_list2 = LinkedList()

# Inserting elements to the linked list
linked_list.insert(0, 1)  # linked_list.insert(data, index)
linked_list.insert(10)
linked_list.insert(20, 1000)
linked_list.insert(30)
linked_list.insert(5, 0)
linked_list.insert(15, 2)
linked_list.insert(40, 5000)
linked_list.print_list()
print("Element {0} found at index {1}.".format(5, linked_list.search(5)))
print("Element {0} found at index {1}.".format(1000, linked_list.search(1000)))
print("Element {0} found at index {1}.".format(20, linked_list.search(20)))


# Inserting and Removing elements from the linked list
linked_list2.delete()
linked_list2.delete(-1000)
linked_list2.delete(10)
linked_list2.insert(0, 1)  # linked_list.insert(data, index)
linked_list2.insert(1, 1)
linked_list2.insert(2, 100)
linked_list2.insert(3)
linked_list2.insert(4)
linked_list2.insert(5)
linked_list2.print_list()
linked_list2.delete(3)
linked_list2.print_list()
linked_list2.delete(100)  # linked_list.delete(index)
linked_list2.print_list()
linked_list2.delete(0)
linked_list2.print_list()
print("Size of the linked list: ", linked_list2.count())
