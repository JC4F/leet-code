"""
1. Brute Force
Time complexity: O(n^2)
Space complexity: O(n)
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max(
            self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)
        )
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))


"""
2. DFS
Time complexity: O(n)
Space complexity: O(h)
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res


"""
3. Iterate DFS
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (
                    1 + max(leftHeight, rightHeight),
                    max(leftHeight + rightHeight, leftDiameter, rightDiameter),
                )

        return mp[root][1]
