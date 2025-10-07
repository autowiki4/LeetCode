class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(0,0):1}
        def dfs(i,j):
            if (i, j) in memo:
                return memo[(i,j)]
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            else:
                val = dfs(i,j-1) + dfs(i-1, j)
                memo[(i,j)] = val
                return val
        return dfs(m-1, n-1)