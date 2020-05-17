# Implementation of a Binary tree
class BinaryTree:
    def __init__(self, value):
        self.element = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, value):
        self.element = value

    def get_root_value(self):
        return self.element

'''
tree = BinaryTree('a')
print(tree.get_root_value())
tree.insert_left('b')
print(tree.get_left_child().get_root_value())
'''
