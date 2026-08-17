class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        
        def union(x, y):
            parX, parY = find(x), find(y)
            if parX == parY:
                return 0
            
            if rank[parX] < rank[parY]:
                par[parX] = parY
                rank[parY] += rank[parX]
            else:
                par[parY] = parX
                rank[parX] += rank[parY]
            
            return 1
        
        res = n
        for x, y in edges:
            res -= union(x, y)
        return res