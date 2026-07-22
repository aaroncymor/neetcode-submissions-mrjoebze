# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):
        dq = deque([(p, q)])
        while dq:
            p, q = dq.popleft()

            if not p and not q:
                continue
            
            if not (p and q and p.val == q.val):
                return False
            
            dq.append((p.left, q.left))
            dq.append((p.right, q.right))
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True 

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )