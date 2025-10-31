class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_id, s_id = 0, 0
        s_len, t_len = len(s), len(t)

        while s_id < s_len and t_id < t_len:
            if s[s_id] == t[t_id]:
                s_id += 1
            t_id += 1
        return s_id == s_len