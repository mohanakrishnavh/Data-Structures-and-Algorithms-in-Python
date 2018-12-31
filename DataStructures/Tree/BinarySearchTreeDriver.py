from Tree.BinarySearchTree import BinarySearchTree


def main():
    bst = BinarySearchTree()
    bst.insert(15)
    bst.insert(10)
    bst.insert(20)
    bst.insert(25)
    bst.insert(8)
    bst.insert(12)

    num = int(input("Enter the number to be searched : "))
    print(bst.search(num))

    print("\nMinimum Value : ", bst.min())
    print("Maximum Value : ", bst.max())

    print("\nMinimum Value (Recursive) : ", bst.min_recursive())
    print("Maximum Value (Recursive) : ", bst.max_recursive())

    print("\nHeight of the tree : ", bst.height())

    print("\nLevel Order Traversal : ")
    bst.level_order_traversal()

    print("\n\nPreorder Traversal : ")
    bst.preorder_traversal()

    print("\n\nInorder Traversal : ")
    bst.inorder_traversal()

    print("\n\nPostorder Traversal : ")
    bst.postorder_traversal()

    print("\n\nIs valid BST ? : ")
    result = bst.is_bst()
    print(result)

    num = int(input("\nEnter the value to delete: "))
    print("Deleting...{0}".format(num))
    bst.delete(num)
    print("{0} found ? : ".format(num), end=" ")
    print(bst.search(num))


if __name__ == '__main__':
    main()
