class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Apply BFS to solve this
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0
        time = 0

        def addfruit(r, c):
            nonlocal  fresh
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] != 1):
                return
            q.append([r, c])
            visit.add((r, c))
            fresh -= 1

        # Collect initial rotten oranges and count fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
        
        # BFS Traversal
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft() 
                addfruit(r + 1, c)
                addfruit(r - 1, c)
                addfruit(r, c + 1)
                addfruit(r, c - 1)
            time += 1
        return time if fresh == 0 else -1

