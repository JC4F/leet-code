"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Input: root = [1,null,2,3]

Output: [1,3,2]
"""


# recursively
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res


def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)


# iteratively
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
