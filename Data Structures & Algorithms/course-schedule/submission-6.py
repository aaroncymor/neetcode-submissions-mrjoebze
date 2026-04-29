class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        q = deque([0])
        visits = set()
        while q:
            crs = q.popleft()
            visits.add(crs)
            for pre in preMap[crs]:
                if pre in visits:
                    return False
                q.append(pre)
        return True