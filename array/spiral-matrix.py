class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        output = []

        i, j = 0, 0

        up, down, left, right = 0, 1, 2, 3
        direct = right

        upwall = 0
        rightwall = cols - 1
        downwall = rows - 1
        leftwall = 0
        while len(output) < rows * cols:
            if direct == right:
                while j <= rightwall:
                    output.append(matrix[i][j])
                    j += 1
                j -= 1
                i += 1
                direct = down
                upwall += 1
            elif direct == down:
                while i <= downwall:
                    output.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                direct = left
                rightwall -= 1
            elif direct == left:
                while j >= leftwall:
                    output.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                direct = up
                downwall -= 1
            else:
                while i >= upwall:
                    output.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                direct = right
                leftwall += 1
        return output                    
