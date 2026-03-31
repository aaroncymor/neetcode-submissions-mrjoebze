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
            return None
        
        heap = []
        for node in lists:
            if not node:
                continue
            heapq.heappush(heap, NodeWrapper(node))
        
        dummy = ListNode()
        cur = dummy
        while heap:
            node_wrapper = heapq.heappop(heap)
            cur.next = ListNode(node_wrapper.node.val)
            cur = cur.next

            if node_wrapper.node.next:
                heapq.heappush(heap, NodeWrapper(node_wrapper.node.next))
        return dummy.next