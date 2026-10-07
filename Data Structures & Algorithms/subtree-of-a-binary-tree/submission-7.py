# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        d = deque([(p, q)])
        while d:
            p, q = d.popleft()
            
            if not p and not q:
                continue
            
            if not (p and q and (p.val == q.val)):
                return False
            
            d.append((p.left, q.left))
            d.append((p.right, q.right))
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subRoot):
            if not subRoot:
                return True
            
            if not root:
                return False
            
            if self.isSameTree(root, subRoot):
                return True

            return (dfs(root.left, subRoot) or dfs(root.right, subRoot))
            
        return dfs(root, subRoot)