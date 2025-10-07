class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        i = 0
        
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            sign = 1
            i = 1
        elif not s[0].isdigit():
            return 0
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        min_val = -2**31
        max_val = 2**31 - 1
        
        if result < min_val:
            return min_val
        elif result > max_val:
            return max_val
        else:
            return result