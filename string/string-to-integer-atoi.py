class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        i = 0

        if s[i] == '-':
            sign = -1
            i = 1
        elif s[i] == '+':
            sign = 1
            i = 1
        elif not s[0].isdigit():
            return 0
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i += 1
        res *= sign
        min_val = -2 **31
        max_val = 2**31 - 1
        if res > max_val:
            return max_val
        elif res < min_val:
            return min_val
        else:
            return res