class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {n:[] for n in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        
        q = deque([crs for crs in adj if indegree[crs] == 0])

        counter = 0
        while q:
            crs = q.popleft()
            counter += 1
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return counter == numCourses