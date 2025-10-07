class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        current = []
        
        def backtrack(start, remaining_sum, remaining_count):
            if remaining_count == 0 and remaining_sum == 0:
                result.append(current[:]) 
                return
            
            if remaining_count == 0 or remaining_sum <= 0:
                return
            
            for num in range(start, 10):
                if num > remaining_sum:
                    break
                current.append(num)
                backtrack(num + 1, remaining_sum - num, remaining_count - 1)
                current.pop()
        
        backtrack(1, n, k)
        return result