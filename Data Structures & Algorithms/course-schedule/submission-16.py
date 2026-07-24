class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hmap[crs].append(pre)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            if hmap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in hmap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            hmap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
