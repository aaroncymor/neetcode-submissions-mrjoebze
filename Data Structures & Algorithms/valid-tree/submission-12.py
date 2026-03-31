class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visits = set()
        q = deque([(0, -1)])
        
        while q:
            i, parent = q.popleft()
            visits.add(i)
            for j in adj[i]:

                if j == parent:
                    continue
                
                if j in visits:
                    return False
                q.append((j, i))

        return len(visits) == n