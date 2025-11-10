class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        original = set([i for i in range(1, n+1)])
        for row in matrix:
            if set(row) != original:
                return False
        for col in range(n):
            if set([matrix[row][col] for row in range(n)]) != original:
                return False
        return True