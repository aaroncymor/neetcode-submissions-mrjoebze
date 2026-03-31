# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def convertToList(root):
            lst = []
            q = [root]
            while q:
                node = q.pop()
                lst.append(-1) if not node else lst.append(node.val)

                if node:
                    q.append(node.left)
                    q.append(node.right)

            return lst

        return convertToList(p) == convertToList(q)

        