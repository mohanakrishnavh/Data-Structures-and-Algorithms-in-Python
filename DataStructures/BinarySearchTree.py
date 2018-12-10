'''
            Average     Worst Case
Space       O(n)         O(n)
Access      O(log n)     O(n)
Search      O(log n)     O(n)
Insertion   O(log n)     O(n)
Deletion    O(log n)     O(n)
'''


class Node:
    def __init__(self, value=None):
        self.element = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.element:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)

        elif value > current_node.element:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)

        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(current_node.element, end=" ")
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left_child, current_height+1)
        right_height = self._height(current_node.right_child, current_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.element:
            return True
        elif value < current_node.element and current_node.left_child is not None:
            return self._search(value, current_node.left_child)
        elif value > current_node.element and current_node.right_child is not None:
            return self._search(value, current_node.right_child)
        return False


def fill_tree(tree, num_elems=50, max_int=1000):
    from random import randint
    for each in range(num_elems):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree


tree = BinarySearchTree()
# tree = fill_tree(tree)
tree.insert(5)
tree.insert(22)
tree.insert(1)
tree.insert(6)
tree.insert(10)
tree.insert(1)
tree.insert(14)
tree.insert(3)
tree.insert(7)
tree.print_tree()
print("\nTree Height: ", tree.height())
print("\nSearch 10. Element found: ", tree.search(10))
print("\nSearch 50. Element found: ", tree.search(50))
