"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

"""
1. Recursion
Time complexity: O(m+n)
Space complexity: O(m+n)
"""


class Solution:
    def add(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int
    ) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, val = divmod(v1 + v2 + carry, 10)

        next_node = self.add(l1.next if l1 else None, l2.next if l2 else None, carry)
        return ListNode(val, next_node)

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.add(l1, l2, 0)


"""
2. Iteration
Time complexity: O(m+n)
Space complexity: O(1)
"""


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
