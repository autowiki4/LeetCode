class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        prev = grid[0][:]
        
        for i in range(1, row):
            cur = [float('inf')] * col
            
            for j in range(col):
                for prev_col in range(col):
                    cost = (prev[prev_col] + 
                        grid[i][j] + 
                        moveCost[grid[i-1][prev_col]][j])
                    cur[j] = min(cur[j], cost)
            
            prev = cur
        
        return min(prev) 