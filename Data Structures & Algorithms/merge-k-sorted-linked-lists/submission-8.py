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
            
            def __lt__(self, other: Optional[ListNode]):
                return self.node.val < other.node.val

        if not lists:
            return None
        
        heap = []
        for lst in lists:
            if not lst:
                continue
            heapq.heappush(heap, NodeWrapper(lst))

        dummy = ListNode()
        curr = dummy
        while heap:
            wrapper = heapq.heappop(heap)
            curr.next = ListNode(wrapper.node.val)
            curr = curr.next

            if wrapper.node and wrapper.node.next:
                heapq.heappush(heap, NodeWrapper(wrapper.node.next))
        return dummy.next