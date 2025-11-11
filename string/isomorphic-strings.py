class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            if sc in s_count:
                if s_count[sc] != tc:
                    return False
            else:
                s_count[sc] = tc
            if tc in t_count:
                if t_count[tc] != sc:
                    return False
            else:
                t_count[tc] = sc
        return True