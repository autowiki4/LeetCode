class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        original = set([i for i in range(1, n+1)])
        columns = [set(original) for _ in range(n)]
        rows = [set(original) for _ in range(n)]

        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                if num not in rows[i]:
                    return False
                rows[i].remove(num)
                if num not in columns[j]:
                    return False
                columns[j].remove(num)
        for hashmap in columns:
            if hashmap:
                return False
        for hashmap in rows:
            if hashmap:
                return False
        return True

