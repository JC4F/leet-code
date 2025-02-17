"""
1. DFS
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)


"""
2. BFS
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root, -float("inf")))

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            if node.left:
                q.append((node.left, max(maxval, node.val)))

            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return res
