class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        inner_box = {}
        for i in range(3):
            inner_box[i] = [set() for _ in range(3)]
        
        for i in range(9):
            curr = set()
            for j in range(9):
                if board[i][j].isnumeric():
                    num = board[i][j]
                    if num in curr:
                        return False
                    curr.add(num)
                    if num in columns[j]:
                        return False
                    columns[j].add(num)
                    if num in inner_box[int(i/3)][int(j/3)]:
                        return False
                    inner_box[int(i/3)][int(j/3)].add(num)
        return True
                    
