class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            a, b = find(n1), find(n2)
            if a == b:
                return 0
            
            if par[b] > par[a]:
                par[a] = b
                rank[b] += rank[a]
            else:
                par[b] = a
                rank[a] += rank[b]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res