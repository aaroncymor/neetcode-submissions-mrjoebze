# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a, b = head, head
        while a and b:
            a = a.next
            b = b.next
            if b:
                b = b.next

            if a and b and (a.val == b.val):
                return True

        return False

        