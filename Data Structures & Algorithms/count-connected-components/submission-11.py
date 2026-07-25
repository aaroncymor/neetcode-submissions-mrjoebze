class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        components = 0
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()

        for i in range(n):
            q = deque([i])
            if i in visited:
                continue
            components += 1
            while q:
                node = q.popleft()
                visited.add(node)
                for j in adj[node]:
                    if j in visited:
                        continue
                    q.append(j)
        return components