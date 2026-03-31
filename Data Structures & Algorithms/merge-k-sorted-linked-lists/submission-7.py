# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
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

        while True:
            if len(lists) == 1:
                return lists[0]
            merged = []          
            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                lst2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeTwoLists(lst1, lst2))
            lists = merged
                
        