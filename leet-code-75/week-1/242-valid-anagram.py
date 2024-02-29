"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:

    Input: s = "rat", t = "car"
    Output: false
"""

# symmetry
# O(n)
from collections import defaultdict

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         length = len(s)
#         if length != len(t):
#             return False

#         for i in range(0, length):
#             if s[i] != t[length - 1 - i]:
#                 return False

#         return True


# class Solution1:
#     def isAnagram(self, s: str, t: str) -> bool:
#         tempS = list(s)
#         length = len(s)
#         midPoint = math.floor(length / 2)

#         for i in range(0, midPoint):
#             temp = tempS[i]
#             tempS[i] = tempS[length - 1 - i]
#             tempS[length - 1 - i] = temp

#         print("".join(tempS))

#         return "".join(tempS) == t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1

        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1

        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False

        return True


solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
