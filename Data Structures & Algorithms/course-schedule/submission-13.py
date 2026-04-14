class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque([i for i in adj if indegree[i] == 0])
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses
