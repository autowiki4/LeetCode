class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(r, c, index):
            if index == len(word):
                return True
            if (r<0 or r>=m or c<0 or c>=n) or  board[r][c] != word[index]:
                return False
            temp = board[r][c]
            board[r][c] = '*'
            for dr, dc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if dfs(dr, dc, index+1):
                    return True
            board[r][c] = temp
            return False
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

