class Solution {
    private int[][] grid;
    private int m;
    private int n;
    private int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    private boolean[][] visited;

    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;
        this.visited = new boolean[m][n];

        int maxArea = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (!visited[r][c] && grid[r][c] == 1) {
                    maxArea = Math.max(maxArea, dfs(r, c));
                }
            
            }
        }
        
        return maxArea;
    }

    public int dfs(int r, int c) {
        if (r < 0 || r >= m || c < 0 || c >= n || visited[r][c] || grid[r][c] == 0) {
            return 0;
        }

        visited[r][c] = true;

        int area = 1;
        for (int[] d: directions) {
            area += dfs(r + d[0], c + d[1]);
        }

        return area;
    }
}