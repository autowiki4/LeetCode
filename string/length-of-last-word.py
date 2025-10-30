class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 and s[0].isalpha():
            return 1
        curr = 0
        last_len = 0
        n = len(s)
        start = n-1
        while s[start] == ' ' and start >= 0:
            start -= 1
        if start == 0:
            return 0
        curr = start
        while s[curr].isalpha():
            curr -= 1
        return start - curr