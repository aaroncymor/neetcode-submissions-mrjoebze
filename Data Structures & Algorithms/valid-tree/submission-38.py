class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = {u:[] for u in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            u, prev = q.popleft()
            for v in adj[u]:
                if v == prev:
                    continue
                if v in visited:
                    return False
                q.append((v, u))
                visited.add(v)
        
        return True if len(visited) == n else False
