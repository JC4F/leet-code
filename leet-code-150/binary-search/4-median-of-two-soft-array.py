"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

"""
1. Brute Force
Time: O((n+m)log(n+m))
Space: O(n+m)
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        totalLen = len(merged)
        if totalLen % 2 == 0:
            return (merged[totalLen // 2 - 1] + merged[totalLen // 2]) / 2.0
        else:
            return merged[totalLen // 2]


"""
2. Two Pointers
Time complexity: O(n+m)
Space complexity: O(1)
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1):
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1

        if (len1 + len2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0


# [1,2,3,4,5,6,7]
# [8,9,10]
# [1,2,3,4,5,6,7,8,9,10]

"""
3. Binary Search
Time complexity: O(log(m+n))
Space complexity: O(log(m+n))
"""


class Solution:
    def get_kth(
        self,
        a: List[int],
        m: int,
        b: List[int],
        n: int,
        k: int,
        a_start: int = 0,
        b_start: int = 0,
    ) -> int:
        if m > n:
            return self.get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0:
            return b[b_start + k - 1]
        if k == 1:
            return min(a[a_start], b[b_start])

        i = min(m, k // 2)
        j = min(n, k // 2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (
            self.get_kth(nums1, len(nums1), nums2, len(nums2), left)
            + self.get_kth(nums1, len(nums1), nums2, len(nums2), right)
        ) / 2.0


"""
4. Binary Search (Optimal)
Time complexity: O(log(min(m,n)))
Space complexity: O(1)
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
