class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        q = deque([(0, -1)])
        while q:
            i, prev = q.popleft()

            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                q.append((j, i))
        return len(visited) == n