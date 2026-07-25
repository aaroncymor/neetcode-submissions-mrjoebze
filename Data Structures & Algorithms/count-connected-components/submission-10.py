class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        components = n
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parents[x] != x:
                top_boss = find(parents[x])
                parents[x] = top_boss
                return parents[x]
            return x
        
        def union(x, y):
            boss_x, boss_y = find(x), find(y)

            if boss_x == boss_y:
                return False

            nonlocal components
            components -= 1

            if rank[boss_x] > rank[boss_y]:
                parents[boss_y] = boss_x
            elif rank[boss_x] < rank[boss_y]:
                parents[boss_x] = boss_y
            else:
                parents[boss_y] = boss_x
                rank[boss_x] += 1
            
            return True

        for x, y in edges:
            union(x, y)

        return components