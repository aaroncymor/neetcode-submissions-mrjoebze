class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        pac_queue = deque()
        atl_queue = deque()
        
        for c in range(COLS):
            pac_queue.append((0, c))
            pac.add((0, c))
            atl_queue.append((ROWS-1, c))
            atl.add((ROWS-1, c))
        
        for r in range(ROWS):
            pac_queue.append((r, 0))
            pac.add((r, 0))
            atl_queue.append((r, COLS-1))
            atl.add((r, COLS-1))
    
        def bfs(queue, visits):
            while queue:
                r, c = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visits and heights[nr][nc] >= heights[r][c]):
                        visits.add((nr, nc))
                        queue.append((nr, nc))
        
        bfs(pac_queue, pac)
        bfs(atl_queue, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res 