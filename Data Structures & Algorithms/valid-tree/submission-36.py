class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
            
        class DSU:

            def __init__(self, n):
                self.par = [i for i in range(n)]
                self.rank = [1] * n
            
            def find(self, n):
                x = n
                while x != self.par[x]:
                    self.par[x] = self.par[self.par[x]]
                    x = self.par[x]
                return x
            
            def union(self, a, b):
                par_a, par_b = self.find(a), self.find(b)
                if par_a == par_b:
                    return 0
                
                if self.rank[par_a] < self.rank[par_b]:
                    self.par[par_a] = par_b
                    self.rank[par_b] += self.rank[par_a]
                else:
                    self.par[par_b] = par_a
                    self.rank[par_a] += self.rank[par_b]
                return 1

        if len(edges) != n - 1:
            return False

        dsu = DSU(n)
        for a, b in edges:
            if dsu.union(a, b) == 0:  # cycle detected
                return False

        return True