from bisect import bisect_left
from typing import List


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
