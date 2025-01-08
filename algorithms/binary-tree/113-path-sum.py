class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root == None:
                return None
            targetSum -= root.val
            path.append(root.val)
            if root.left == None and root.right == None:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        ans = []
        dfs(root, targetSum, [])
        return ans


# another way => trick to not use backtracking
def pathSum(self, root, sum):
    res = []
    self.dfs(root, sum, [], res)
    return res


def dfs(self, root, sum, ls, res):
    if root:
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        self.dfs(root.left, sum - root.val, ls + [root.val], res)
        self.dfs(root.right, sum - root.val, ls + [root.val], res)


# DFS + stack I
def pathSum4(self, root, sum):
    if not root:
        return []
    res = []
    stack = [(root, sum - root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
        if curr.left:
            stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
    return res
