# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root):
            vals = []
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node:
                    vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    vals.append(None)
            return vals

        return dfs(p) == dfs(q)

        