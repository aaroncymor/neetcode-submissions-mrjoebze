class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        components = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            components += 1
            q = deque([i])
            while q:
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for j in adj[node]:
                    q.append(j)
        return components
