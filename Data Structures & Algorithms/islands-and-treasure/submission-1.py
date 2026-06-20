class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        inf = 2^32 - 1
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dx, dy in directions:
                    if (r + dx >= 0 and c + dy >= 0 and r + dx < rows and c + dy < cols and 
                    (r + dx, c + dy) not in visited and grid[r + dx][c + dy] != -1):
                        q.append((r + dx, c + dy))
                        visited.add((r + dx, c + dy))
            dist += 1
                        

                            
