class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
from typing import List


class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        # Set to track visited coordinates (row, col) to avoid redundant checks and cycles
        visit = set()

        # Min-heap to store [max_elevation_so_far, row, col]
        # Always pops the cell reachable with the minimum time/elevation so far (Dijkstra's approach)
        minh = [[grid[0][0], 0, 0]]

        # Movement directions: right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Mark starting cell as visited
        visit.add((0, 0))

        while minh:
            # Pop the path with the current minimum required time
            t, r, c = heapq.heappop(minh)

            # Reached destination (bottom-right cell)
            if r == N - 1 and c == N - 1:
                return t

            # Explore all 4 adjacent neighbors
            for dr, dc in directions:
                neir, neic = r + dr, c + dc

                # Skip out-of-bounds coordinates or already visited cells
                if (
                    neir < 0
                    or neic < 0
                    or neir == N
                    or neic == N
                    or (neir, neic) in visit
                ):
                    continue

                # Mark neighbor as visited immediately to prevent duplicate heap entries
                visit.add((neir, neic))

                # Push neighbor to heap with updated time: max of current path time and target cell height
                heapq.heappush(
                    minh, [max(t, grid[neir][neic]), neir, neic]
                )