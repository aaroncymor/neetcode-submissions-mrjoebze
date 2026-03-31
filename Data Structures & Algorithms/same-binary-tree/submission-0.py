# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False

        p_vals = []
        q_vals = []
        qp = [p]
        qq = [q]

        while qp and qq:
            np = qp.pop(0)
            nq = qq.pop(0)

            if np:
                p_vals.append(np.val)
            else:
                p_vals.append(None)

            if nq:
                q_vals.append(nq.val)
            else:
                q_vals.append(None)

            if np:
                qp.append(np.left)
                qp.append(np.right)

            if nq:
                qq.append(nq.left)
                qq.append(nq.right)
        return p_vals == q_vals
        