class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        if len(s) < len(p):
            return indices
        p_count = {}
        s_count = {}
        for c in p:
            p_count[c] = p_count.get(c, 0) + 1
        l, r = 0, len(p)-1
        for i in range(l, r+1):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
        if s_count == p_count:
            indices.append(l)
        
        while r + 1 < len(s):
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                del s_count[s[l]]
            l += 1
            r += 1
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            if s_count == p_count:
                indices.append(l)
        return indices

        