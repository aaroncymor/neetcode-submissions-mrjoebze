class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = [i for i in range(n + 1)]
        self.Size = [1] * (n + 1)
    
    def find(self, n1):
        if self.Parent[n1] != n1:
            self.Parent[n1] = self.find(self.Parent[n1])
        return self.Parent[n1]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        self.comps -= 1
        if self.Size[pv] > self.Size[pu]:
            pu, pv = pv, pu
        self.Parent[pv] = pu
        self.Size[pu] += self.Size[pv]
        return True
    
    def components(self):
        return self.comps


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for n1, n2 in edges:
            if not dsu.union(n1, n2):
                return False
        return dsu.components() == 1