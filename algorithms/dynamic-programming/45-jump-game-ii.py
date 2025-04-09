"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""

"""
1. Recursion
Time complexity: O(n!)
Space complexity: O(n)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float("inf")

            end = min(len(nums) - 1, i + nums[i])
            res = float("inf")
            for j in range(i + 1, end + 1):
                res = min(res, 1 + dfs(j))
            return res

        return dfs(0)


"""
2. DP (Top-down)
Time complexity: O(n^2)
Space complexity: O(n)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return 1000000

            res = 1000000
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            memo[i] = res
            return res

        return dfs(0)


"""
3. DP (Bottom-up)
Time complexity: O(n^2)
Space complexity: O(n)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1000000] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]


"""
4. Greedy
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
