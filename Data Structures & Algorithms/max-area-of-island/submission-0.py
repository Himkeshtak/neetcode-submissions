class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = ([1, 0], [0, 1], [-1, 0], [0, -1])
        total_area, max_area = 0,0
        def dfs(r, c):
            nonlocal total_area
            if( r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0
            total_area += 1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                total_area = 0
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, total_area)
        return max_area
