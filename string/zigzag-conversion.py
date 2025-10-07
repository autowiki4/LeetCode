class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        constant = 2 * numRows - 2
        output = ''

        def add_constant(start, output_string, rows):
            index = start
            while index < len(s):
                output_string += s[index]
                # For rows in between the first and last
                middle = index + constant - 2 * start
                if start > 0 and start < rows - 1 and middle < len(s):
                    output_string += s[middle]
                index += constant
            return output_string

        for row in range(numRows):
            output = add_constant(row, output, numRows)
        
        return output


        