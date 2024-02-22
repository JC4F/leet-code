from typing import List

# sort => modified the original object
# sorted => create a sorted copy


# wrong index after sort
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)  # Use sorted() to create a sorted copy
        i = 0
        j = len(sorted_nums) - 1  # Adjusted the index for the last element

        while i < j:
            if sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            elif sorted_nums[i] + sorted_nums[j] == target:
                return [i, j]

        return []


solution = Solution()

# Test Case 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))


# solution O(n) using hash table
# Solution 2: (Two-pass Hash Table)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found


# Solution 3: (One-pass Hash Table)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
