class DSU:
    def __init__(self, n):
        self.Parent = [i for i in range(n + 1)]
        self.Size = [1] * (n + 1)

    def find(self, n1):
        if n1 != self.Parent[n1]:
            self.Parent[n1] = self.find(self.Parent[n1])
        return self.Parent[n1]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.Size[p2] > self.Size[p1]:
            self.Parent[p1] = p2
            self.Size[p2] += self.Size[p1]
        else:
            self.Parent[p2] = p1
            self.Size[p1] = self.Size[p2]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for n1, n2 in edges:
            if dsu.union(n1, n2):
                return True
        return False