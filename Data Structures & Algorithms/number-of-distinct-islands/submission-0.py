class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        seen_shapes = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        #DFS algo
        curr_hash = []
        def dfs(s_row, s_col, row, col):
            #get hash number relative to s_row and s_col
            diff_r = s_row - row
            diff_c = s_col - col
            hash_val = diff_r * COLS + diff_c
            curr_hash.append(hash_val)
            grid[row][col] = 0
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if (0 <= new_r < ROWS) and (0 <= new_c < COLS) and grid[new_r][new_c] == 1:
                    dfs(s_row, s_col, new_r, new_c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_hash = []
                    dfs(r, c, r, c)
                    seen_shapes.add(tuple(curr_hash))
        
        return len(seen_shapes)