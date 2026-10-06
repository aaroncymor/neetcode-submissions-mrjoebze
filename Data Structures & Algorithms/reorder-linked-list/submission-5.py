# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = head, head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        
        second = first.next
        prev = first.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            second.next = first.next
            first.next = second
            first, second = t1, t2