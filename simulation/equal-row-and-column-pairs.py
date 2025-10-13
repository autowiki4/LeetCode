class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        equal = {}
        for row in grid:
            row_tuple = tuple(row)
            equal[row_tuple] = equal.get(row_tuple, 0) + 1
        pairs = 0
        for i in range(n):
            col = [grid[j][i] for j in range(n)]
            col_tuple = tuple(col)
            if col_tuple in equal:
                pairs += equal[col_tuple]
        return pairs
