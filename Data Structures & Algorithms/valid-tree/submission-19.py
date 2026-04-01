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
            node, par = q.popleft()
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visited:
                    return False
                q.append((nei, node))
        return len(visited) == n