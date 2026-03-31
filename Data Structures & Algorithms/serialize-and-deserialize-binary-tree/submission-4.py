# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
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
        lst = data.split(",")
        self.ctr = 0

        def dfs():
            if lst[self.ctr] == "N":
                self.ctr += 1
                return None
            
            root = TreeNode(int(lst[self.ctr]))
            self.ctr += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
