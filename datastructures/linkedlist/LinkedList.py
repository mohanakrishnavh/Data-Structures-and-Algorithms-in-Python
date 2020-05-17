class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        """
        :return: Head of the Linked List
        """
        return self.head

    def insert(self, data: int, index=None) -> None:
        """
        Inserting a new element to the Linked List
        :param data: Data of the new element
        :param index: Index to insert
        :return: None

        Time Complexity: O(n)
        """

        is_valid_index = isinstance(index, int)

        if is_valid_index and index >= 0:
            self._insert_at_index(data, index)
        else:
            self._insert_at_tail(data)

    def _insert_at_index(self, data: int, index: int) -> None:
        """
        Inserting a new element at the given index of the Linked List
        :param data: Data of the new element
        :param index: Index to insert
        :return: None

        Time Complexity: O(n)
        """
        # If the list is empty
        if self.head is None:
            self.head = Node(data)
            return

        # If the user wants to insert at the first position
        if index == 0:
            self._insert_at_head(data)
        else:
            new_node = Node(data)
            current_node = self.head
            previous_node = self.head

            for i in range(index-1):
                # If the user has provided an index greater than the size of the list
                if current_node is None:
                    previous_node.next = new_node
                    return

                previous_node = current_node
                current_node = current_node.next

            new_node.next = current_node.next
            previous_node = current_node
            previous_node.next = new_node

    def _insert_at_tail(self, data: int) -> None:
        """
        Inserting an element at the end of the Linked List
        :param data: Data of the new node
        :return: None

        Time Complexity: O(n)
        """
        new_node = Node(data)
        current_node = self.head

        # If there are no elements in the linked list
        if self.head is None:
            self.head = new_node
            return

        # Traversing the elements of the list to find the last element
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def _insert_at_head(self, data) -> None:
        """
        Inserts a new node at the head of the Linked List
        :param data: Data of the new node
        :return: None

        Time Complexity: O(1)
        """
        new_node = Node(data)
        prev_head = self.head

        # Make the new node the head of the linked list and add link to old head
        new_node.next = prev_head
        self.head = new_node

    def delete(self, index=None) -> None:
        """
        Delete an element from the Linked List
        :param index: Index of the element to delete
        :return: None

        Time Complexity: O(n)
        """
        # If the list is empty, do not do anything
        if self.head is None:
            return

        is_valid_index = isinstance(index, int)

        if is_valid_index and index >= 0:
            self._delete_from_index(index)
        else:
            self._delete_from_tail()

    def _delete_from_head(self) -> None:
        """
        Delete an element from the head of the Linked List
        :return: None

        Time Complexity: O(1)
        """
        new_head = self.head.next
        self.head = new_head

    def _delete_from_tail(self) -> None:
        """
        Delete an element from the tail of the Linked List
        :return: None

        Time Complexity: O(n)
        """
        current_node = self.head
        previous_node = None

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None

    def _delete_from_index(self, index: int) -> None:
        """
        Delete an element from the the specified index of the Linked List
        :return: None

        Time Complexity: O(n)
        """
        if index == 0:
            self._delete_from_head()
        else:
            current_node = self.head
            previous_node = None

            for i in range(index):
                # If the user has provided an index greater than the size of the list
                if current_node.next is None:
                    previous_node.next = None
                    return

                previous_node = current_node
                current_node = current_node.next

            previous_node.next = current_node.next
            current_node.next = None

    def search(self, x) -> int:
        """
        Search an element in the Linked List
        :param x: Element to search
        :return: Index of the element if found

        Time Complexity: O(n)
        """
        if self.head is None:
            return -1

        current_node = self.head
        result = 0

        while current_node is not None:
            if current_node.data == x:
                return result

            current_node = current_node.next
            result += 1

        return -1

    def count(self) -> int:
        """
        Returns the count/size of the Linked List
        :return: Size/Count of the Linked List

        Time Complexity: O(n)
        """
        count = 0

        if self.head is None:
            count = 0
        else:
            current_node = self.head
            while current_node is not None:
                current_node = current_node.next
                count += 1

        return count

    def print_list(self, head=None) -> None:
        """
        Prints the elements in the list
        :return: None

        Time Complexity: O(n)
        """

        current_node = head if (head is not None) else self.head

        # If the linked list is empty
        if current_node is None:
            return

        while current_node.next is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print(current_node.data)
