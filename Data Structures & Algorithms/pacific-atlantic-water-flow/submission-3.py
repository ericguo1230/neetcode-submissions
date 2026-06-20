class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        res = []
        mp = {(0, len(heights[0]) - 1): True, 
        (len(heights) - 1, 0): True}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(heights), len(heights[0])

        def isAtlantic(r, c):
            if r == len(heights) - 1 and (0 <= c < len(heights[0])):
                return True
            elif c == len(heights[0]) - 1 and (0 <= r < len(heights)):
                return True
            return False
        
        def isPacific(r, c):
            if r == 0 and (0 <= c < len(heights[0])):
                return True
            elif c == 0 and (0 <= r < len(heights)):
                return True
            return False

        def isValid(r, c):
            res = [0, 0]
            visited = set()
            q = deque()
            q.append((r, c))
            while q:
                y, x = q.popleft()
                if isPacific(y, x):
                    res[0] = 1
                if isAtlantic(y, x):
                    res[1] = 1
                if res == [1, 1]:
                    return True
                for dr, dc in directions:
                    dr_y, dc_x = y + dr, x + dc
                    if (dr_y, dc_x) in mp and heights[dr_y][dc_x] <= heights[y][x]:
                        if mp[(dr_y, dc_x)] == True:
                            return True
                    
                    if (dr_y, dc_x) not in visited and (-1 < dr_y < row) and (-1 < dc_x < col) and heights[dr_y][dc_x] <= heights[y][x]:
                        visited.add((dr_y, dc_x))
                        q.append((dr_y, dc_x))
            return False

        for r in range(row):
            for c in range(col):
                if isValid(r, c):
                    mp[(r, c)] = True
                    res.append([r, c])
                else:
                    mp[(r, c)] = False
        return res
        
                