class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        memo = {(0,0):1}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(i,j):
            if (i, j) in memo:
                return memo[(i,j)]
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                val = 0
                memo[(i,j)] = val
                return val
            else:
                val = dfs(i,j-1) + dfs(i-1, j)
                memo[(i,j)] = val
                return val
        return dfs(m-1, n-1)