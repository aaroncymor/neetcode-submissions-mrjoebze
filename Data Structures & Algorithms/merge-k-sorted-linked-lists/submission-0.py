# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeList(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not lists:
                return None

            if len(lists) == 1:
                return lists[0]

            # # assumes more than one list node
            merged = lists[0]
            # merged = self.mergeList(lists[0], lists[1])
            for node in lists[1:]:
                merged = self.mergeList(merged, node)

            return merged

