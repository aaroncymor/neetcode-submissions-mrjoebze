class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def bfs():
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

            return True
        
        return bfs() and len(visited) == n