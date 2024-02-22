from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for item in nums:
            s.add(item)

        return len(s) != len(nums)


solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 4]))
