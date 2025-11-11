class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_count = {}
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        return len(s_count) == len(t_count)