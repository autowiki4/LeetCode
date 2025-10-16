class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        integer = 0
        n = len(s)
        i, j = 0, 1
        while i < n:
            if j >= n:
                integer += roman[s[i]]
                break
            after = roman[s[j]]
            before = roman[s[i]]
            if after > before:
                integer += after-before
                i += 2
                j += 2
            else:
                integer += before
                i += 1
                j += 1
        return integer