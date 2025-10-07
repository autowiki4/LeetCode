class Solution:
    def tribonacci(self, n: int) -> int:
        f, s, t = 0, 1, 1
        if n == 0:
            return n
        if n == 1 or n == 2:
            return 1
        for _ in range(3, n+1):
            f, s, t = s, t, f+s+t
        return t
        