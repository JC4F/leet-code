"""
https://leetcode.com/problems/trapping-rain-water/solutions/1374608/c-java-python-maxleft-maxright-so-far-with-picture-o-1-space-clean-concise/?envType=problem-list-v2&envId=dynamic-programming

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

"""
Solution 1: Max Left, Max Right So Far!

    A ith bar can trap the water if and only if there exists a higher bar to the left and a higher bar to the right of ith bar.
    To calculate how much amount of water the ith bar can trap, we need to look at the maximum height of the left bar and the maximum height of the right bar, then
        The water level can be formed at ith bar is: waterLevel = min(maxLeft[i], maxRight[i])
        If waterLevel >= height[i] then ith bar can trap waterLevel - height[i] amount of water.
    To achieve in O(1) when looking at the maximum height of the bar on the left side and on the right side of ith bar, we pre-compute it:
        Let maxLeft[i] is the maximum height of the bar on the left side of ith bar.
        Let maxRight[i] is the maximum height of the bar on the right side of ith bar.
        
=> Complexity
    Time: O(N), where N <= 3*10^4 is number of bars.
    Space: O(N)
        
"""

from ast import List


class Solution:  # 52 ms, faster than 81.89%
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n

        for i in range(1, n):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(height[i + 1], maxRight[i + 1])

        ans = 0
        for i in range(n):
            waterLevel = min(maxLeft[i], maxRight[i])
            if waterLevel >= height[i]:
                ans += waterLevel - height[i]
        return ans


"""
 Solution 2: Two Pointers

    Same idea with solution 1, but now we don't need to build maxLeft and maxRight arrays, we will calculate maxLeft and maxRight as we go.
    We start with maxLeft = height[0], maxRight = height[n-1], using 2 pointers left point to the next bar on the left side, right point to the next bar on the right side.
    How to decide to move left or move right?
        If maxLeft < maxRight, it means the water level is based on the left side (the left bar is smaller) then move left side:
            If height[left] > maxLeft then there is no trap water, we update maxLeft by maxLeft = height[left].
            Else if height[left] < maxLeft then it can trap an amount of water, which is maxLeft - height[left].
            Move left by left += 1
        Else if maxLeft > maxRight, it means the water level is based on the right side (the right bar is smaller) then move right side:
            If height[right] > maxRight then there is no trap water, we update maxRight by maxRight = height[right].
            Else if height[right] < maxRight then it can trap an amount of water, which is maxRight - height[right].
            Move right by right -= 1.

Complexity
    Time: O(N), where N <= 3*10^4 is number of bars.
    Space: O(1)
"""


class Solution:  # 48 ms, faster than 92.74%
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        n = len(height)
        maxLeft, maxRight = height[0], height[n - 1]
        left, right = 1, n - 2
        ans = 0
        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1
        return ans
