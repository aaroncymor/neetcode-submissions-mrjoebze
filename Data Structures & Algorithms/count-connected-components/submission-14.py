class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.Parents = [i for i in range(n)]
                self.Rank = [1] * n
            
            def find(self, u):
                while u != self.Parents[u]:
                    self.Parents[u] = self.Parents[self.Parents[u]]
                    u = self.Parents[u]
                return u
            
            def union(self, u, v):
                parU, parV = self.find(u), self.find(v)
                if parU == parV:
                    return 0
                
                if self.Rank[parU] < self.Rank[parV]:
                    self.Parents[parU] = parV
                    self.Rank[parV] += self.Rank[parU]
                else:
                    self.Parents[parV] = parU
                    self.Rank[parU] += self.Rank[parV]
                return 1
        
        dsu = DSU(n)
        res = n
        for u, v in edges:
            res -= dsu.union(u, v)
        return res
