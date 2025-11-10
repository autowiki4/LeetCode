class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def count_neighbors(i, j):
            count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if board[ni][nj] in [1, 2]:
                            count += 1
            return count
        
        
        for i in range(m):
            for j in range(n):
                neighbors = count_neighbors(i, j)
                
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 2
                else:
                    if neighbors == 3:
                        board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
        