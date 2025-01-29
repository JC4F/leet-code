"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
1. Recursion
Time complexity: 0(n)
Space complexity: 0(n)
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead


"""
2. Iterative
Time complexity: 0(n)
Space complexity: 0(1)
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = None
        while head is not None:
            tmp: ListNode = head.next
            head.next = result
            result = head
            head = tmp

        return result
