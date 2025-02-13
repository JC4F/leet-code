"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


# Solution - I (Brute-Force) [TLE]
class Solution:
    def uniquePaths(self, m, n, i=0, j=0):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        return self.uniquePaths(m, n, i + 1, j) + self.uniquePaths(m, n, i, j + 1)


#  Solution - II (Dynamic Programming - Memoization)
class Solution:
    def uniquePaths(self, m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)


# Solution - III (Dynamic Programming - Tabulation)
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1] * n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# Solution - IV (Space Optimized Dynamic Programming)
# class Solution:
#     def uniquePaths(self, m, n):
#         dp = [[1] * n for i in range(2)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j - 1]
#         return dp[(m - 1) & 1][-1]

"""
The above solution runs in O(m * n) time and costs O(m * n) space. However, you may have noticed that each time when we update dp[i][j], we only need dp[i - 1][j] (at the previous row) and dp[i][j - 1] (at the current row). So we can reduce the memory usage to just two rows (O(n)).

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> pre(n, 1), cur(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                cur[j] = pre[j] + cur[j - 1];
            }
            swap(pre, cur);
        }
        return pre[n - 1];
    }
};

Further inspecting the above code, pre[j] is just the cur[j] before the update. So we can further reduce the memory usage to one row.

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> cur(n, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                cur[j] += cur[j - 1];
            }
        }
        return cur[n - 1];
    }
};
"""
