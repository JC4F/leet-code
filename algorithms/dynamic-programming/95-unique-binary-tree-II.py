"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
=>
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
"""

"""
# divide and conquer
=> ideal same as problem 96
====> G(i) ~ list node left, right => then combine

public List<TreeNode> generateTrees(int n) {
	return generateSubtrees(1, n);
}

private List<TreeNode> generateSubtrees(int s, int e) {
	List<TreeNode> res = new LinkedList<TreeNode>();
	if (s > e) {
		res.add(null); // empty tree
		return res;
	}

	for (int i = s; i <= e; ++i) {
		List<TreeNode> leftSubtrees = generateSubtrees(s, i - 1);
		List<TreeNode> rightSubtrees = generateSubtrees(i + 1, e);

		for (TreeNode left : leftSubtrees) {
			for (TreeNode right : rightSubtrees) {
				TreeNode root = new TreeNode(i);
				root.left = left;
				root.right = right;
				res.add(root);
			}
		}
	}
	return res;
}
"""
