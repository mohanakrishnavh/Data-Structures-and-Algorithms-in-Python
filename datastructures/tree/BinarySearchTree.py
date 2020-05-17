import sys
from queue import Queue


class Node:
    def __init__(self, data):
        '''
        Creates a new node with left and right pointers pointing to None
        :param data: data of the new node
        '''
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        '''
        Initializes the root
        '''
        # set the root as empty
        self.root = None

    def insert(self, data):
        '''
        Function to insert a new node
        :param data: value of the new node
        '''
        # if root is NULL - tree is empty
        if self.root is None:
            self.root = Node(data)

        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        '''
        Helper function to insert a node recursively
        :param node: current node
        :param data:
        :return:
        '''
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)

        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def search(self, data):
        '''
        Function to search for a value
        :param data: data to search
        :return: True if the value is found
        '''
        if self.root is None:
            return False

        else:
            return self._search(self.root, data)

    def _search(self, node, data):
        '''
        Helper function to search for a value in the tree
        :param node: current node
        :param data: data to search
        :return: True if the value is found, else False
        '''
        if data == node.data:
            return True

        elif data <= node.data and node.left is not None:
            return self._search(node.left, data)

        elif data > node.data and node.right is not None:
            return self._search(node.right, data)

        else:
            return False

    def min(self):
        '''
        Function to find the minimum value
        :return: minimum value in the tree
        '''
        if self.root is None:
            print("tree is empty!")
            return -1

        current = self.root
        while current.left is not None:
            current = current.left

        return current.data

    def min_node(self):
        '''
        Function to find the minimum value
        :return: minimum value in the tree
        '''
        if self.root is None:
            print("tree is empty!")
            return -1

        current = self.root
        while current.left is not None:
            current = current.left

        return current

    def min_recursive(self):
        '''
        Function to find the minimum value recursively
        :return: minimum value in the tree
        '''
        return self._min_recursive(self.root)

    def _min_recursive(self, node):
        '''
        Helper function to find the minimum value recursively
        '''
        if self.root is None:
            print("tree is empty!")
            return -1

        elif node.left is None:
            return node.data

        return self._min_recursive(node.left)

    def max(self):
        '''
        Function to find the maximum value
        :return: maximum value in the tree
        '''

        if self.root is None:
            print("tree is empty!")
            return -1

        current = self.root
        while current.right is not None:
            current = current.right

        return current.data

    def max_recursive(self):
        '''
        Function to find the maximum value recursively
        :return: maximum value in the tree
        '''
        return self._max_recursive(self.root)

    def _max_recursive(self, node):
        '''
        Helper function to find the maximum value recursively
        '''
        if self.root is None:
            print("tree is empty!")
            return -1

        elif node.right is None:
            return node.data

        return self._max_recursive(node.right)

    def height(self):
        '''
        Computes the height of the tree
        :return: height of the tree
        '''
        return self._height(self.root)

    def _height(self, node):
        '''
        Helper function to compute the height of the tree
        :param node: current node
        :return: height of a node
        '''
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return 1 + max(left_height, right_height)

    def level_order_traversal(self):
        '''
        Level Order Traversal
        Time Complextiy : O(n)
        Space Complexity : O(n) (worst case), O(1) (best case)
        '''
        if self.root is None:
            return

        q = Queue()
        q.put(self.root)

        while q.empty() is not True:
            current = q.get()
            print(current.data, end=" ")
            if current.left is not None:
                q.put(current.left)

            if current.right is not None:
                q.put(current.right)

    def preorder_traversal(self):
        '''
        Preorder Treaversal
        Time Complexity : O(n)
        Space Complexity : O(h) [worst case O(n), bast/average case O(log n)]
        '''
        if self.root is None:
            return
        else:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        '''
        Helper function to perform preorder traversal
        '''
        print(node.data, end= " ")

        if node.left is not None:
            self._preorder_traversal(node.left)

        if node.right is not None:
            self._preorder_traversal(node.right)

    def inorder_traversal(self):
        '''
        Inorder Treaversal
        Time Complexity : O(n)
        Space Complexity : O(h) [worst case O(n), bast/average case O(log n)]
        '''
        if self.root is None:
            return
        else:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        '''
        Helper function to perform inorder traversal
        '''

        if node.left is not None:
            self._inorder_traversal(node.left)

        print(node.data, end=" ")

        if node.right is not None:
            self._inorder_traversal(node.right)

    def postorder_traversal(self):
        '''
        Postorder Treaversal
        Time Complexity : O(n)
        Space Complexity : O(h) [worst case O(n), bast/average case O(log n)]
        '''
        if self.root is None:
            return
        else:
            self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        '''
        Helper function to perform postorder traversal
        '''
        if node.left is not None:
            self._postorder_traversal(node.left)

        if node.right is not None:
            self._postorder_traversal(node.right)

        print(node.data, end=" ")

    def is_bst(self):
        '''
        Function to check if the given tree is a Binary Search tree
        :return: True if it BST, else False

        Time Complexity : O(n)
        '''
        min_val = -sys.maxsize
        max_val = sys.maxsize
        result = self.is_bst_util(self.root, min_val, max_val)
        return result

    def is_bst_util(self, node, min_val, max_val):
        '''
        Helper function to check if it is BST
        :param node: current
        :param min_val: min value the node can take
        :param max_val: max value the node can take
        :return: if current node is a BST or not
        '''
        if node is None:
            return True

        if min_val < node.data < max_val and self.is_bst_util(node.left, min_val, node.data) and self.is_bst_util(node.right, node.data, max_val):
            return True

        else:
            return False

    def delete(self, data):
        return self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node

        elif data < node.data:
            node.left = self._delete(node.left, data)

        elif data > node.data:
            node.right = self._delete(node.right, data)

        else:
            # Case 1 : No child
            if node.left is None and node.right is None:
                del node
                node = None

            # Case 2 : One child
            elif node.left is None:
                temp = node
                node = node.right
                del temp

            elif node.right is None:
                temp = node
                node = node.left
                del temp

            # Case 3 : Two children
            else:
                temp = self.node.right.min_node()
                node.data = temp.data
                node.right = self._delete(node.right, temp.data)

            return node