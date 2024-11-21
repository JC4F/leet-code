"""
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.
"""

"""
 Solution 1: Top down DP
Time: O(N), where N <= 100 is length of string s.
Space: O(N)
For a character s[i], we have 2 ways to decode:
Single digit: Require s[i] != '0' (decoded to 1..9)
Two digits: Require i + 1 < len(s) and (s[i] == 1 (decoded to 10..19) or s[i] == 2 and s[i+1] <= '6') (decoded to 20..26).
"""
from functools import lru_cache  # noqa: E402


class Solution:  # 36 ms, faster than 34.07%
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return 1
            ans = 0
            if s[i] != "0":  # Single digit
                ans += dp(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] <= "6"
            ):  # Two digits
                ans += dp(i + 2)
            return ans

        return dp(0)


"""
✔️ Solution 2: Bottom-up DP

Just convert from Top-down DP to Bottom-up DP approach.
Complexity

Time: O(N), where N <= 100 is length of string s.
Space: O(N)

"""


class Solution:  # 28 ms, faster than 88.10%
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] != "0":  # Single digit
                dp[i] += dp[i + 1]
            if i + 1 < n and (
                s[i] == "1" or s[i] == "2" and s[i + 1] <= "6"
            ):  # Two digits
                dp[i] += dp[i + 2]
        return dp[0]


"""
Solution 3: Bottom-up DP (Space Optimized)

Since our dp only need to keep up to 3 following states:
Current state, let name dp corresponding to dp[i]
Last state, let name dp1 corresponding to dp[i+1]
Last twice state, let name dp2 corresponding to dp[i+2]
So we can achieve O(1) in space.
Complexity

Time: O(N), where N <= 100 is length of string s.
Space: O(1)
"""


class Solution:  # 24 ms, faster than 96.81%
    def numDecodings(self, s: str) -> int:
        dp, dp1, dp2, n = 0, 1, 0, len(s)
        for i in range(n - 1, -1, -1):
            if s[i] != "0":  # Single digit
                dp += dp1
            if i + 1 < n and (
                s[i] == "1" or s[i] == "2" and s[i + 1] <= "6"
            ):  # Two digits
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
