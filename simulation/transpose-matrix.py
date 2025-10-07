class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        old_rows = {}
        for row in matrix:
            for col in range(len(row)):
                if col in old_rows:
                    old_rows[col].append(row[col])
                else:
                    old_rows[col] = [row[col]]
        return list(old_rows.values())
        
        