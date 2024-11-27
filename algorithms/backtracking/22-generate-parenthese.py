"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.curr_stack = []

    def helper(self, L, R):
        if R == 0:
            self.ans.append("".join(self.curr_stack))
            return
        if R > L:
            self.curr_stack.append(")")
            self.helper(L, R - 1)
            self.curr_stack.pop()
        if L > 0:
            self.curr_stack.append("(")
            self.helper(L - 1, R)
            self.curr_stack.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.helper(n, n)
        return self.an


# another solution:
def generateParenthesis(self, n: int) -> List[str]:
    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return

        if left < n:
            dfs(left + 1, right, s + "(")

        if right < left:
            dfs(left, right + 1, s + ")")

    res = []
    dfs(0, 0, "")
    return res


"""
								   	(0, 0, '')
								 	    |	
									(1, 0, '(')  
								   /           \
							(2, 0, '((')      (1, 1, '()')
							   /                 \
						(2, 1, '(()')           (2, 1, '()(')
						   /                       \
					(2, 2, '(())')                (2, 2, '()()')
						      |	                             |
					res.append('(())')             res.append('()()')
   
"""
