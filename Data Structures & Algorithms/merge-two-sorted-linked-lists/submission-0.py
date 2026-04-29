# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = list1, list2
        merged = ListNode(None, None)
        result = merged

        while a and b:

            if a.val <= b.val:
                merged.next = ListNode(a.val)
                merged = merged.next
                merged.next = ListNode(b.val)
            else:
                merged.next = ListNode(b.val)
                merged = merged.next
                merged.next = ListNode(a.val)

            a = a.next
            b = b.next
            merged = merged.next

        if a:
            merged.next = list1

        if b:
            merged.next = list2

        return result.next


        