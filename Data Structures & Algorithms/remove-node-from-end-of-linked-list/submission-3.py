# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head):
            curr = head
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        prev = reverseList(head)

        dummy = ListNode()
        tail = dummy

        i = 1
        while prev:
            if i == n:
                prev = prev.next
                i += 1
                continue
            tail.next = ListNode(prev.val, None)
            tail = tail.next
            prev = prev.next
            i += 1

        return reverseList(dummy.next)

        