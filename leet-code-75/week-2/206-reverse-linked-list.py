'''

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = None
        while head is not None:  
            tmp: ListNode = head.next
            head.next = result
            result = head
            head = tmp
        
        return result