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


"""
* DP (Bottom-up)
* Time complexity: O(n^2)
* Space complexity: O(n)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


"""
* Segment tree
* Time complexity: O(n * log(n))
* Space complexity: O(n)
"""
from bisect import bisect_left


class SegmentTree:
    def __init__(self, N):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.tree = [0] * (2 * self.n)

    def update(self, i, val):
        self.tree[self.n + i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1

    def query(self, l, r):
        if l > r:
            return 0
        res = float("-inf")
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(arr):
            sortedArr = sorted(set(arr))
            order = []
            for num in arr:
                order.append(bisect_left(sortedArr, num))
            return order

        nums = compress(nums)
        n = len(nums)
        segTree = SegmentTree(n)

        LIS = 0
        for num in nums:
            curLIS = segTree.query(0, num - 1) + 1
            segTree.update(num, curLIS)
            LIS = max(LIS, curLIS)
        return LIS


"""
* DP + Binary Search (bisect_left)
* Time complexity: O(n * log(n))
* Space complexity: O(n)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS
