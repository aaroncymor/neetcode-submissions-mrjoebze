class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = {crs: 0 for crs in range(numCourses)}
        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)

        print("INDEGREE", indegree)
        q = deque([crs for crs in range(len(adj)) if indegree[crs] == 0])
        print("QUEUE", q)
        print("ADJ", adj)
        finish = 0
        while q:
            crs = q.popleft()
            finish += 1
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        return numCourses == finish