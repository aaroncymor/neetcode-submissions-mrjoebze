# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        d = deque([(p, q)])
        while d:
            p, q = d.popleft()
            if not p and not q:
                continue

            if not (p and q and p.val == q.val):
                return False
            
            d.append((p.left, q.left))
            d.append((p.right, q.right))

        return True