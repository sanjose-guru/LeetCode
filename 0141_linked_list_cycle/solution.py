# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p, fast_p = head, head
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
            slow_p = slow_p.next
        return False
