class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def preOrder(root):
    while root:
        # If left child is null, print the current
        # node data. Move to right child.
        if root.left is None:
            print(root.data, end=" ")
            root = root.right
        else:
            # Find inorder predecessor
            current = root.left
            while current.right and current.right != root:
                current = current.right

            # If the right child of inorder predecessor
            # already points to this node
            if current.right == root:
                current.right = None
                root = root.right

            # If right child doesn't point to this node, then print this
            # node and make right child point to this node
            else:
                print(root.data, end=" ")
                current.right = root
                root = root.left


if __name__ == "__main__":
    # Constructing binary tree.
    #
    #             1
    #            / \
    #           /   \
    #          2     3
    #         / \   / \
    #        /   \ /   \
    #       4    5 6    7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    preOrder(root)
    print()
