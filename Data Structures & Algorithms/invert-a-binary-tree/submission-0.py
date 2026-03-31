# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return curr
        