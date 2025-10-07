class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cols, rows = len(matrix), len(matrix[0])
        output = []

        i, j = 0, 0

        up, down, left, right = 0, 1, 2, 3
        direction = right

        upwall = 0
        downwall = cols - 1
        leftwall = 0
        rightwall = rows - 1

        while len(output) < rows * cols:
            if direction == right:
                while j <= rightwall:
                    output.append(matrix[i][j])
                    j += 1
                j -= 1
                i += 1
                direction = down
                upwall += 1
            elif direction == down:
                while i <= downwall:
                    output.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                direction = left
                rightwall -= 1
            elif direction == left:
                while j >= leftwall:
                    output.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                direction = up
                downwall -= 1
            elif direction == up:
                while i >= upwall:
                    output.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                direction = right
                leftwall += 1
        return output