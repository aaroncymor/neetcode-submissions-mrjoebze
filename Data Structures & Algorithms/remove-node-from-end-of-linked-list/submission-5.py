# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseL(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        nhead = reverseL(head)
        tmp = ListNode()
        curr = tmp
        i = 1
        while nhead:
            if i == n:
                nhead = nhead.next
                i += 1
                continue
            tmp.next = ListNode(nhead.val, None)
            tmp = tmp.next
            nhead = nhead.next
            i += 1
        return reverseL(curr.next)

        