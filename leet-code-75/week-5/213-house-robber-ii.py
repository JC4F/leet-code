"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [3,4,3]

Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.
"""

"""
1. Recursion
Time complexity: O(2^n)
Space complexity: O(n)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))

        return max(dfs(0, True), dfs(1, False))


"""
2. Dynamic Programming (Top-Down)
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(
                dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or (i == 0))
            )
            return memo[i][flag]

        return max(dfs(0, True), dfs(1, False))


"""
3. DP (Bottom-up)
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


"""
4. Dynamic Programming (Space Optimized)
Time complexity: O(n)
 pace complexity: O(1)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
