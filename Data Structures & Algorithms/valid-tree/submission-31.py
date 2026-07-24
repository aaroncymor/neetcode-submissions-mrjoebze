class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hmap = {i: [] for i in range(n)}
        for i, j in edges:
            hmap[i].append(j)
            if j not in hmap:
                hmap[j] = []
            if i in hmap[j]:
                continue
            hmap[j].append(i)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in hmap[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n