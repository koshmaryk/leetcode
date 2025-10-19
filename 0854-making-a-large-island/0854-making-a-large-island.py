class Solution:
    '''
    0 0
    0 0

    1 0
    0 1

    10 0
    0  11

    1 1
    1 1

    '''
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, curr_idx):
            if not (0 <= r < n and 0 <= c < n) or grid[r][c] != 1:
                return 0

            grid[r][c] = curr_idx

            size = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                size += dfs(nr, nc, curr_idx)
            return size 

        sizes = {} # 10->1, 11->1
        idx = 10
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    sizes[idx] = dfs(r, c, idx) # 1 | 1
                    idx += 1 # 11

        if not sizes:
            return 1 # 0 -> 1

        ans = max(sizes.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    visited = set()
                    size = 1

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            visited.add(grid[nr][nc])
                    
                    for n_idx in visited:
                        size += sizes[n_idx]

                    ans = max(ans, size)
        return ans
