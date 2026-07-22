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
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
            maxLevel += 1
        return maxLevel

