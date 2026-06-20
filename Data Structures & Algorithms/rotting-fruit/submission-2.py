class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        counter = 0
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    counter += 1
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        minutes = 0
        change = 0
        while q:
            if change == counter:
                return minutes
            for l in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if x >=0 and y >=0 and x < rows and y < cols and (x , y) not in visit and grid[x][y] == 1:
                        change += 1
                        q.append((x, y))
                        visit.add((x, y))
            minutes += 1
        return minutes if change == counter else -1
        

