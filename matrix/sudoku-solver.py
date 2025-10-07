class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    box = (r // 3)*3 + (c // 3)
                    boxes[box].add(num)
                else:
                    empty_cells.append((r,c))
        def backtrack(idx):
            if idx == len(empty_cells):
                return  True
            r, c = empty_cells[idx]
            box = (r // 3)*3 + (c // 3)
            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)
                    if backtrack(idx+1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)
            return False
        backtrack(0)

        