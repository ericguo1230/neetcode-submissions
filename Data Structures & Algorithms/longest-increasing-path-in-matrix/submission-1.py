class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = 1
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < ROWS and 0 <= col < COLS and matrix[row][col] > matrix[r][c]:
                    res = max(res, 1 + dfs(row, col))
            cache[(r, c)] = res
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res