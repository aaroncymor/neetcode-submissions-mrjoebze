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
        maxLevel = 0
        q = deque([(root, 1)])
        while q:
            node, lvl = q.popleft()
            maxLevel = max(maxLevel, lvl)
            if node and node.left:
                q.append((node.left, lvl + 1))

            if node and node.right:
                q.append((node.right, lvl + 1))
        return maxLevel