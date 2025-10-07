class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n == 2:
            return n
        prev = 1
        curr = 2

        for _ in range(3, n + 1):
            prev, curr = curr, curr + prev
        
        return curr