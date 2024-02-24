"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    

    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

    

    Constraints:

        1 <= prices.length <= 105
        0 <= prices[i] <= 104

"""
from typing import List


# bad solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                maxP = max([maxP, prices[j] - prices[i]])

        return maxP


# base Kadane’s Algorithm
"""
    Suppose we have original array:
    [a0, a1, a2, a3, a4, a5, a6]

    what we are given here(or we calculate ourselves) is:
    [b0, b1, b2, b3, b4, b5, b6]

    where,
    b[i] = 0, when i == 0
    b[i] = a[i] - a[i - 1], when i != 0

    suppose if a2 and a6 are the points that give us the max difference (a2 < a6)
    then in our given array, we need to find the sum of sub array from b3 to b6.

    b3 = a3 - a2
    b4 = a4 - a3
    b5 = a5 - a4
    b6 = a6 - a5

    adding all these, all the middle terms will cancel out except two
    i.e.

    b3 + b4 + b5 + b6 = a6 - a2

    a6 - a2 is the required solution.
"""


# better
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        curMax, maxSoFar = 0, 0

        for i in range(1, len(prices)):
            curMax += prices[i] - prices[i - 1]
            curMax = max([0, curMax])
            maxSoFar = max([maxSoFar, curMax])

        return maxSoFar


#
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        ans = 0
        n = len(prices)

        for i in range(1, n):
            ans = max(ans, prices[i] - minSoFar)
            minSoFar = min(minSoFar, prices[i])

        return ans


solution = Solution()

print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
