class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        n = len(haystack)
        for i in range(n-length+1):
            if haystack[i:i+length] == needle:
                return i
        return -1
