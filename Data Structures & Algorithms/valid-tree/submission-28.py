class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = [i for i in range(n + 1)]
        self.Size = [1] * (n + 1)

    def find(self, n1):
        if n1 != self.Parent[n1]:
            self.Parent[n1] = self.find(self.Parent[n1])
        return self.Parent[n1]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.comps -= 1

        if self.Size[pu] > self.Size[pv]:
            self.Parent[pu] = pv
            self.Size[pv] += self.Size[pu]
        else:
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
        for p, u in edges:
            if not dsu.union(p, u):
                return False

        return dsu.components() == 1
