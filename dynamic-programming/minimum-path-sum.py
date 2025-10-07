class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        memo = {(0,0):grid[0][0]}
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return float('inf')
            if (i,j) in memo:
                return memo[(i,j)]
            new = grid[i][j] + min(dfs(i-1, j), dfs(i, j-1))
            memo[(i,j)] = new
            return new
        return dfs(m-1, n-1)