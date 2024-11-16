"""
To calculate the number of ways to climb the stairs, we can observe that when we are on the nth stair,
we have two options:
  1.either we climbed one stair from the (n-1)th stair or
  2.we climbed two stairs from the (n-2)th stair.
By leveraging this observation, we can break down the problem into smaller subproblems and apply the concept of the Fibonacci series.
The base cases are when we are on the 1st stair (only one way to reach it) and the 2nd stair (two ways to reach it).
By summing up the number of ways to reach the (n-1)th and (n-2)th stairs, we can compute the total number of ways to climb the stairs. This allows us to solve the problem efficiently using various dynamic programming techniques such as recursion, memoization, tabulation, or space optimization.
"""


# solution 1: Recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# solution 2: Memorization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]


# solution 3: tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# solution 4: space optimzation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
