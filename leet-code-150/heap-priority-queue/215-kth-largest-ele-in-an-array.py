"""
Description
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:

Input: nums = [2,3,1,5,4], k = 2

Output: 4
"""

"""
1. Sorting
Time complexity: O(nlogn)
Space complexity: O(1) or O(n) depending on the sorting algorithm
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


"""
2. Min-Heap
Time complexity: O(nlogk)
Space complexity: O(k)
"""


class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


"""
3. Quick Select
Time complexity: O(n) on average, O(n^2) in the worst case
Space complexity: O(n)
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
