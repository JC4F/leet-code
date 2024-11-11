'''
root = (root.left, root.right)[p.val > root.val]
is a compact way of writing an if-else statement using a tuple and an index. Let’s break down what it does:

Explanation
Tuple Creation: (root.left, root.right) creates a tuple containing root.left and root.right.
Index Selection: [p.val > root.val] evaluates the expression p.val > root.val:
If p.val > root.val is True, it evaluates to 1 (because True is treated as 1 in Python).
If p.val > root.val is False, it evaluates to 0 (because False is treated as 0 in Python).
'''

# solution 1: Iterative O(1) space
def lowestCommonAncestor(self, root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = (root.left, root.right)[p.val > root.val]
    return root

def lowestCommonAncestor(self, root, p, q):
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root
        
# solution 2: Recursive

def lowestCommonAncestor(self, root, p, q):
    next = p.val < root.val > q.val and root.left or \
           p.val > root.val < q.val and root.right
    return self.lowestCommonAncestor(next, p, q) if next else root