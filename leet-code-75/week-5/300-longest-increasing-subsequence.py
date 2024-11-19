"""
300. Longest Increasing Subsequence
Medium
Topics
Companies
Given an integer array nums, return the length of the longest strictly increasing
subsequence

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

# solution 1: Dynamic Programming
"""
Complexity
Time: O(N^2), where N <= 2500 is the number of elements in array nums.
Space: O(N)
"""
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/

from ast import List
from bisect import bisect_left  # noqa: E402


class Solution:  # 2516 ms, faster than 64.96%
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


# Solution 2: Greedy with Binary Search
"""
Complexity:

Time: O(N * logN)
Space: O(N)
"""


class Solution:  # 68 ms, faster than 93.92%
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)


# Get Longest Increasing Subsequence Path
class Solution:
    def pathOfLIS(self, nums: List[int]):
        sub = []
        subIndex = []  # Store index instead of value for tracing path purpose
        trace = [-1] * len(
            nums
        )  # trace[i] point to the index of previous number in LIS
        for i, x in enumerate(nums):
            if len(sub) == 0 or sub[-1] < x:
                if subIndex:
                    trace[i] = subIndex[-1]
                sub.append(x)
                subIndex.append(i)
            else:
                idx = bisect_left(
                    sub, x
                )  # Find the index of the smallest number >= x, replace that number with x
                if idx > 0:
                    trace[i] = subIndex[idx - 1]
                sub[idx] = x
                subIndex[idx] = i

        path = []
        t = subIndex[-1]
        while t >= 0:
            path.append(nums[t])
            t = trace[t]
        return path[::-1]


print(Solution().pathOfLIS([2, 6, 8, 3, 4, 5, 1]))  # [2, 3, 4, 5]


# Solution 3: Binary Indexed Tree (Increase BASE of nums into one-base indexing)
# ===> giống ở chỗ là đều tìm những cái nằm bên trái của mảng
"""
Time: O(N * logN)
Space: O(N)
"""


class MaxBIT:  # One-based indexing
    def __init__(self, size):
        self.bit = [0] * (size + 1)

    def get(self, idx):
        ans = 0
        while idx > 0:
            ans = max(ans, self.bit[idx])
            idx -= idx & (-idx)
        return ans

    def update(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & (-idx)


class Solution:  # 360 ms, faster than 69.28%
    def lengthOfLIS(self, nums: List[int]) -> int:
        bit = MaxBIT(20001)
        BASE = 10001
        for x in nums:
            subLongest = bit.get(BASE + x - 1)
            bit.update(BASE + x, subLongest + 1)
        return bit.get(20001)


print(Solution().lengthOfLIS([2, 6, 8, 3, 4, 5, 1]))  # [2, 3, 4, 5]

#  Solution 4: Binary Indexed Tree (Compress nums into values in [1...N])
# quite hard ^_^


#  Solution 5: Segment Tree
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 4 * self.n

    # query (qleft, qright) to find maximum elements in range [qleft...qright]
    def query(self, left, right, index, qleft, qright):
        if qright < left or qleft > right:
            return 0

        if qleft <= left and right <= qright:
            return self.tree[index]

        mid = (left + right) // 2
        resLeft = self.query(left, mid, 2 * index + 1, qleft, qright)
        resRight = self.query(mid + 1, right, 2 * index + 2, qleft, qright)
        return max(resLeft, resRight)

    # update an element at `pos` to `val`
    def update(self, left, right, index, pos, val):
        if left == right:
            self.tree[index] = val
            return

        mid = (left + right) // 2
        if pos <= mid:
            self.update(left, mid, 2 * index + 1, pos, val)
        else:
            self.update(mid + 1, right, 2 * index + 2, pos, val)
        self.tree[index] = max(self.tree[2 * index + 1], self.tree[2 * index + 2])


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(
            arr,
        ):  # Example: [1, 9999, 20, 10, 20] -> Expected: [0, 3, 2, 1, 2]
            sortedArr = sorted(arr)
            ans = []
            for x in arr:
                ans.append(bisect_left(sortedArr, x))
            return ans

        nums = compress(nums)
        n = len(nums)
        segmentTree = SegmentTree(n)
        for x in nums:
            subLongest = segmentTree.query(0, n - 1, 0, 0, x - 1)
            segmentTree.update(0, n - 1, 0, x, subLongest + 1)
        return segmentTree.query(0, n - 1, 0, 0, n - 1)
