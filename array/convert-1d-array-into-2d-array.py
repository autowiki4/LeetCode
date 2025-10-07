class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != (m*n):
            return []
        
        converted_array = []
        for start in range(0, len(original) - n + 1, n):
            converted_array.append(original[start:start + n])
        
        return converted_array