"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
# https://leetcode.com/problems/word-break/description/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        @lru_cache(None)
        def dp(start):
            if start == n:  # Found a valid way to break words
                return True

            for end in range(start + 1, n + 1):  # O(N^2)
                word = s[start:end]  # O(N)
                if word in wordSet and dp(end):
                    return True
            return False

        return dp(0)


"""
Where n is the length of the string m is the number of words in wordDict and t is the maximum length of any word in wordDict.
"""

"""
1. Recursion
Time complexity: O(t * m^n)
Space complexity: O(n)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True

            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True
            return False

        return dfs(0)


"""
2. Dynamic Programming (Bottom-Up)
Time complexity: O(n * m * t)
Space complexity: O(n)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


"""
3. DP (Trie)
Time complexity: O((n * t^2) + m)
Space complexity: O(n + (m*t))
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        t = 0
        for w in wordDict:
            t = max(t, len(w))

        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]
