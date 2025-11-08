class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        target_freq = {}
        for c in t:
            target_freq[c] = target_freq.get(c, 0) + 1
        req = len(target_freq)
        formed = 0
        curr = {}
        l = 0
        min_l = 0
        min_len = float('inf')

        for r in range(len(s)):
            c = s[r]
            curr[c] = curr.get(c, 0) + 1
            if c in target_freq and curr[c] == target_freq[c]:
                formed += 1
            while l <= r and formed == req:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_l = l
                char = s[l]
                curr[char] -= 1
                if char in target_freq and curr[char] < target_freq[char]:
                    formed -= 1
                l += 1
        return '' if min_len == float('inf') else s[min_l:min_l + min_len]
