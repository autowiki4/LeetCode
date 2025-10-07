class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        count = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] in count and count[s[r]] >= l:
                l = count[s[r]] + 1
            count[s[r]] = r
            max_len = max(max_len, r-l+1)
        return max_len