class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_items = [set() for _ in range(9)]

        inner_box_columns = {}
        for i in range(3):
            inner_box_columns[i] = [set() for _ in range(3)]

        for i in range(9):
            digit_set = set()
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in digit_set:
                        return False
                    digit_set.add(board[i][j])
                    if board[i][j] in column_items[j]:
                        return False
                    column_items[j].add(board[i][j])

                    if board[i][j] in inner_box_columns[int(i / 3)][int(j / 3)]:
                        return False
                    inner_box_columns[int(i / 3)][int(j / 3)].add(board[i][j])
        return True



        for i in range(0, 9, 3):
            column_items
