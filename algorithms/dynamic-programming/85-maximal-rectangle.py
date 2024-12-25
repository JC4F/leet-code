"""
# dp + monoptonic stack

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
"""

"""
❌ Solution - I (Brute-Force)

The most brute force way of solving this problem would be to simply consider each and every possible rectangle and consider the maximal out of the rectangles which only consists of 1 in them

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& M) {
        if(!size(M)) return 0;
        int ans = 0, m = size(M), n = size(M[0]);
        for(int start_i = 0; start_i < m; start_i++) 
            for(int start_j = 0; start_j < n; start_j++) 
                for(int end_i = start_i; end_i < m; end_i++) 
                    for(int end_j = start_j; end_j < n; end_j++) {
                        bool allOnes = true;
                        for(int i = start_i; i <= end_i && allOnes; i++) 
                            for(int j = start_j; j <= end_j && allOnes; j++) 
                                if(M[i][j] != '1') allOnes = false;                           
                        ans = max(ans, allOnes * (end_i - start_i + 1) * (end_j - start_j + 1));
                    }

        return ans;
    }
};
Time Complexity : O((MN)3)
Space Complexity : O(1)
"""

"""
 Solution - II (Optimized Brute-Force)
 class Solution {
public:
    int maximalRectangle(vector<vector<char>>& M) {
        if(!size(M)) return 0;
        int ans = 0, m = size(M), n = size(M[0]);
        for(int i = 0; i < m; i++) 
            for(int j = 0; j < n; j++) 
                for(int row = i, colLen = n, col; row < m && M[row][j] == '1'; row++) {
                    for(col = j; col < n && M[row][col] == '1'; col++);
                    colLen = min(colLen, col-j);
                    ans = max(ans, (row-i+1) * colLen);
                }
            
        return ans;
    }
};
Time Complexity : O((MN)2)
Space Complexity : O(1)
"""

"""
Solution - III (Pre-compute consecutive 1s to the right / DP)
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& M) {
        if(!size(M)) return 0;
        int ans = 0, m = size(M), n = size(M[0]);
        vector<vector<short>> dp(m+1, vector<short>(n+1));
        for(int i = m-1; ~i; i--) 
            for(int j = n-1; ~j; j--) 
                dp[i][j] = M[i][j] == '1' ? dp[i][j+1] + 1 : 0;
                    
        for(int i = 0; i < m; i++) 
            for(int j = 0; j < n; j++) 
                for(int row = i, colLen = n; row < m && M[row][j] == '1'; row++)
                    ans = max(ans, (row-i+1) * (colLen = min(colLen, dp[row][j]*1)));
                    
        return ans;
    }
};
Time Complexity : O(M2N)
Space Complexity : O(MN)
"""

"""
 Solution - IV (Pre-compute consecutive 1s to right + number of rows above & below having atleast same number of consecutive 1s / DP)
 class Solution {
public:
    int maximalRectangle(vector<vector<char>>& M) {
        if(!size(M)) return 0;
        int ans = 0, m = size(M), n = size(M[0]);
        vector<vector<short>> dp(m+1, vector<short>(n+1)), up(m, vector<short>(n,1)), down(up);
        for(int i = m-1; ~i; i--) 
            for(int j = n-1; ~j; j--) 
                dp[i][j] = M[i][j] == '1' ? dp[i][j+1] + 1 : 0;
        
        stack<int> s;
        for(int j = 0; j < n; j++) {
            s = stack<int>();
            for(int i = 0; i < m; i++) {
                while(size(s) && dp[s.top()][j] >= dp[i][j]) s.pop();
                up[i][j] = i - (size(s) ? s.top() : -1);
                s.push(i);
            }
            s = stack<int>();
            for(int i = m-1; ~i; i--) {
                while(size(s) && dp[s.top()][j] >= dp[i][j]) s.pop();
                down[i][j] = (size(s) ? s.top() : m) - i;
                s.push(i);
            }            
        }

        for(int i = 0; i < m; i++) 
            for(int j = 0; j < n; j++) 
                ans = max(ans, dp[i][j] * (up[i][j]+down[i][j]-1));
                    
        return ans;
    }
};
Time Complexity : O(MN)
Space Complexity : O(MN)
"""
