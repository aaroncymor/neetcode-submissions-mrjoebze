# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def helper(node, depth):
            if not node:
                return

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            helper(node.left, depth+1)
            helper(node.right, depth+1)

        helper(root, 0)
        return res
