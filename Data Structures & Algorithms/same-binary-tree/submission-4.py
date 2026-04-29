# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([(p, q)])
        while q:
            a, b = q.popleft()
            if not a and not b:
                return True
            if (not a or not b) or ((a and b) and (a.val != b.val)):
                return False
            q.append((a.left, b.left))
            q.append((a.right, b.right))
        return True