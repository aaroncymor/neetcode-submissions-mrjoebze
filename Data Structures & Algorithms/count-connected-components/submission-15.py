class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in adj[i]:
                dfs(nei)
            return
        
        count = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            count += 1
        return count