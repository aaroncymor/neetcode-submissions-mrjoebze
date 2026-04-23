class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([(0, -1)])
        visited = set()
        visited.add(0)
        while q:
            i, prev = q.popleft()
            for j in adj[i]:
                if j == prev:
                    continue
                
                if j in visited:
                    return False
                visited.add(j)
                q.append((j, i))
        return len(visited) == n
