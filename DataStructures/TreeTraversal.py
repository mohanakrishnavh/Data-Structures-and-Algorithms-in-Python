from BinaryTree import BinaryTree


def preorder(node):
    if node is not None:
        print(node.get_root_value())
        preorder(node.get_left_child())
        preorder(node.get_right_child())


def inorder(node):
    if node is not None:
        inorder(node.get_left_child())
        print(node.get_root_value())
        inorder(node.get_right_child())


def postorder(node):
    if node is not None:
        postorder(node.get_left_child())
        postorder(node.get_right_child())
        print(node.get_root_value())


tree = BinaryTree(10)
tree.insert_left(8)
tree.insert_right(12)
l = tree.get_left_child()
l.insert_left(6)
l.insert_right(7)
r = tree.get_right_child()
r.insert_left(11)
r.insert_right(13)

print("Preorder Traversal: ")
preorder(tree)
print()

print("Inorder Traversal: ")
inorder(tree)
print()

print("Postorder Traversal: ")
postorder(tree)
print()


