# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class NodeContainer:
            def __init__(self, node):
                self.node = node
            
            def __lt__(self, other):
                return self.node.val < other.node.val
            
        heap = []
        for node in lists:
            if not node:
                continue
            heapq.heappush(heap, NodeContainer(node))

        dummy = ListNode()
        tail = dummy
        while heap:
            node_container = heapq.heappop(heap)
            tail.next = node_container.node
            tail = tail.next
            if not node_container.node.next:
                continue
            heapq.heappush(heap, NodeContainer(node_container.node.next))
        
        return dummy.next
        