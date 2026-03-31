# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        if not root:
            return 0

        q = [(root, 1)]

        while q:
            node, lvl = q.pop(0)
            maxD = max(maxD, lvl)

            if node and node.left:
                q.append((node.left, lvl + 1))

            if node and node.right:
                q.append((node.right, lvl + 1))
        return maxD

        