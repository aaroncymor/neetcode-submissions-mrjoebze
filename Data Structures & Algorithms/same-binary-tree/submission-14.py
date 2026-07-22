# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def valid(p, q):

            if not p and not q:
                return True
            
            if not (p and q and p.val == q.val):
                return False
            
            return (
                valid(p.left, q.left) and
                valid(p.right, q.right)
            )
        
        return valid(p, q)
