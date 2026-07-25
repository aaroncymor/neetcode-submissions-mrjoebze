class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                top_boss = find(parent[x])
                parent[x] = top_boss
                return parent[x]
            return x
        
        def union(x, y):
            boss_x, boss_y = find(x), find(y)
            if boss_x == boss_y:
                return 0
            
            if rank[boss_x] > rank[boss_y]:
                parent[boss_y] = boss_x
            elif rank[boss_x] < rank[boss_y]:
                parent[boss_x] = boss_y
            else:
                parent[boss_y] = boss_x
                rank[boss_x] += 1
            return -1
        
        components = n
        for x, y in edges:
            components += union(x, y)
        return components