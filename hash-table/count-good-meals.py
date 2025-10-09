class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = {}
        count = 0
        powers = [1 << i for i in range(22)]
        MOD = 10**9 + 7
        for meal in deliciousness:
            for power in powers:
                comp = power-meal
                if comp in freq:
                    count = (count + freq[comp]) % MOD
            freq[meal] = freq.get(meal, 0) + 1
        return count