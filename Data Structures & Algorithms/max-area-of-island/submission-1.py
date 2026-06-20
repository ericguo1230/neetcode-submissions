class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_island = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(x, y) -> int:
            island = 1
            stack = [(x, y)]
            visit.add((x, y))
            while stack:
                r, c = stack.pop()
                for dx, dy in directions:
                    dr, dc = r + dx, c + dy
                    if (dr >= 0 and dr < rows and dc >= 0 and dc < cols and grid[dr][dc] == 1 and (dr, dc) not in visit):
                        stack.append((dr, dc))
                        visit.add((dr, dc))
                        island += 1
            return island

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_island = max(max_island, bfs(r, c))
        return max_island
        
        