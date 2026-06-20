class Solution {
    private static final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int numIslands(char[][] grid) {
        if (grid.length == 0){
            return 0;
        }
        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;
        for (int i = 0; i < rows; i ++){
            for (int j = 0; j < cols; j ++){
                if (grid[i][j] == '1'){
                    backTrack(grid, i, j);
                    islands ++;
                }
            }
        }
        return islands;
    }

    private void backTrack(char[][] grid, int x, int y){
        Queue<int[]> visit = new LinkedList<>();
        grid[x][y] = '0';
        visit.add(new int[]{x, y});
        while (!visit.isEmpty()){
            int[] current = visit.poll();
            int row = current[0], col = current[1];
            for (int i = 0; i < directions.length; i ++){
                int nr = row + directions[i][0], nc = col + directions[i][1];
                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] == '1'){
                    visit.add(new int[]{nr, nc});
                    grid[nr][nc] = '0';
                }
            }
        }
    }
}
