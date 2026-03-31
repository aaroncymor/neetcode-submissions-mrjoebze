# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoSorted(self, a, b):
        dummy = ListNode()
        tail = dummy
        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        if a:
            tail.next = a
        elif b:
            tail.next = b
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        while lists:
            if len(lists) == 1:
                return lists[0]
            
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoSorted(l1, l2))
            lists = merged