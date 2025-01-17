"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, m * n - 1
        while l != r:
            mid = (l + r - 1) // 2
            if matrix[mid // m][mid % m] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[r // m][r % m] == target
