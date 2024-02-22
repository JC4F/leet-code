from typing import List

# sort => modified the original object
# sorted => create a sorted copy


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
