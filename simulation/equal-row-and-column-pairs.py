class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = {}
        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1
        
        equal = 0
        for c in range(n):
            col_tuple = tuple(grid[i][c] for i in range(n))
            if col_tuple in row_count:
                equal += row_count[col_tuple]
        
        return equal