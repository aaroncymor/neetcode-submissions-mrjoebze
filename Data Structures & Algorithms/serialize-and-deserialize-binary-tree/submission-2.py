# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        lst = []
        def dfs(node):
            if not node:
                lst.append("N")
                return
            
            lst.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(lst)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if self.i >= len(vals):
                return

            if vals[self.i] == "N":
                self.i += 1
                return
            
            root = TreeNode(vals[self.i])
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
    
        return dfs()

