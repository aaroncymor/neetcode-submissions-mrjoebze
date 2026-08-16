class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacq, atlq = deque(), deque()
        pac, atl = set(), set()
        res = []

        for c in range(COLS):
            pacq.append((0, c))
            pac.add((0, c))
            atlq.append((ROWS - 1, c))
            atl.add((ROWS - 1, c))

        for r in range(ROWS):
            pacq.append((r, 0))
            pac.add((r, 0))
            atlq.append((r, COLS - 1))
            atl.add((r, COLS - 1))
        
        def bfs(q, visits):
            while q:
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        nr in range(ROWS) and nc in range(COLS) and
                        (nr, nc) not in visits and heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
                        visits.add((nr, nc))
        
        bfs(pacq, pac)
        bfs(atlq, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

