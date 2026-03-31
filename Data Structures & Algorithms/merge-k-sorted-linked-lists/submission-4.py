# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class NodeWrapper:
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        if not lists:
            return

        heap = []
        for ln in lists:
            if ln:
                heapq.heappush(heap, NodeWrapper(ln))

        dummy = ListNode()
        curr = dummy

        while heap:
            nw = heapq.heappop(heap)
            curr.next = ListNode(nw.node.val)
            curr = curr.next

            if nw.node.next:
                heapq.heappush(heap, NodeWrapper(nw.node.next))

        return dummy.next

