class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = ''
        for c in s:
            if c.isalnum():
                s_lower += c.lower()
        n = len(s_lower)
        mid = n // 2
        for i in range(mid):
            if s_lower[i] != s_lower[-i-1]:
                return False
        return True