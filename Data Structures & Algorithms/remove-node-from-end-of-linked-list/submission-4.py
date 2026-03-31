# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0, head)
        left, right = tmp, head

        i = 0
        while right and n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        if left.next:
            left.next = left.next.next
        return tmp.next
        