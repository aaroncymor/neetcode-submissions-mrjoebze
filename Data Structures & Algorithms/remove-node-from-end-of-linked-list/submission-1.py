# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head):
            curr, prev = head, None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        # reverse 1
        reversed = reverseList(head)
        # print("reversed"), reversed
        dummy = ListNode()
        tail = dummy
        i = 1
        while reversed:
            if i == n:
                reversed = reversed.next
                i += 1
                continue
            i += 1
            tail.next = ListNode(reversed.val, None)
            reversed = reversed.next
            tail = tail.next

        orig = reverseList(dummy.next)
        return orig


        