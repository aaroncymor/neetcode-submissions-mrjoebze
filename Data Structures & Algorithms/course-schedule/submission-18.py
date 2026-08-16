class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { n: [] for n in range(numCourses) }
        indegree = { n: 0 for n in range(numCourses) }

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        
        q = deque([n for n in adj if indegree[n] == 0])
        print("Q", q)
        visited = set()
        while q:
            crs = q.popleft()
            visited.add(crs)
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
                    
        return len(visited) == numCourses