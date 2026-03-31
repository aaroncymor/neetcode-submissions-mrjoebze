# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def preorder(node):
            nonlocal res
            if not node:
                res += "N,"
                return
            res += str(node.val) + ","
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nums = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if nums[i] == "N":
                i += 1
                return
            root = TreeNode(int(nums[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()