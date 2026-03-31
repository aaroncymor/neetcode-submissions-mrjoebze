# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxD = 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if not node:
                continue
            maxD = max(maxD, depth)
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        return maxD

        