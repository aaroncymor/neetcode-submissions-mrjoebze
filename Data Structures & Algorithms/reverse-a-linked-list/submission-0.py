# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr, prev):
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            return helper(curr, prev)

        val = helper(head, None)
        return val
