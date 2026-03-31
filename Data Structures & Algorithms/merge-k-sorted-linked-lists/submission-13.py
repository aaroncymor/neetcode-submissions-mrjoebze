# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class NodeWrapper:

    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        heap = []
        for node in lists:
            if not node:
                continue
            heapq.heappush(heap, NodeWrapper(node))
        
        cur = ListNode()
        tail = cur
        while heap:
            wrapper = heapq.heappop(heap)
            node = wrapper.node
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))
        return cur.next
        