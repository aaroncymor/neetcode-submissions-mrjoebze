class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        q = deque([(0, -1)])
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