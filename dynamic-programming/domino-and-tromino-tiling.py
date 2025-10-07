class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n <= 2:
            return n
        
        # f[i] = ways to fully tile 2×i board
        # p[i] = ways to partially tile 2×i board (one cell uncovered)
        f = [0] * (n + 1)
        p = [0] * (n + 1)
        
        f[0] = 1  # Base case: empty board
        f[1] = 1  # One vertical domino
        f[2] = 2  # Two ways: two horizontal or two vertical
        p[2] = 1  # One tromino leaves one cell uncovered
        
        for i in range(3, n + 1):
            f[i] = (f[i-1] + f[i-2] + 2 * p[i-1]) % MOD
            p[i] = (f[i-2] + p[i-1]) % MOD
        
        return f[n]