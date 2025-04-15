"""
You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

Every left parenthesis '(' must have a corresponding right parenthesis ')'.
Every right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
Example 1:

Input: s = "((**)"

Output: true
Explanation: One of the '*' could be a ')' and the other could be an empty string.
"""

"""
1. Recursion
Time complexity: O(3^n)
Space complexity: O(n)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if s[i] == "(":
                return dfs(i + 1, open + 1)
            elif s[i] == ")":
                return dfs(i + 1, open - 1)
            else:
                return dfs(i + 1, open) or dfs(i + 1, open + 1) or dfs(i + 1, open - 1)

        return dfs(0, 0)


"""
2. Dynamic Programming
Time complexity: O(n^2)
Space complexity: O(n^2)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[None] * (n + 1) for _ in range(n + 1)]

        def dfs(i, open):
            if open < 0:
                return False
            if i == n:
                return open == 0
            if memo[i][open] is not None:
                return memo[i][open]

            if s[i] == "(":
                result = dfs(i + 1, open + 1)
            elif s[i] == ")":
                result = dfs(i + 1, open - 1)
            else:
                result = (
                    dfs(i + 1, open) or dfs(i + 1, open + 1) or dfs(i + 1, open - 1)
                )

            memo[i][open] = result
            return result

        return dfs(0, 0)


"""
3. Stack
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False
        return not left


"""
4. Greedy
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
