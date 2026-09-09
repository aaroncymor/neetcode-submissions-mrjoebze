class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def bfs(i):
            q = deque([i])
            visited.add(i)
            while q:
                i = q.popleft()
                for nei in adj[i]:
                    if nei in visited:
                        continue
                    q.append(nei)
                    visited.add(nei)
        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        return count