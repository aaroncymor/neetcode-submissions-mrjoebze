# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(cur, p, q):
            if cur.val > p.val and cur.val > q.val:
                return dfs(cur.left, p, q)
            elif cur.val < p.val and cur.val < q.val:
                return dfs(cur.right, p, q)
            else:
                return cur
        return dfs(root, p, q)