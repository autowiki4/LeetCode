class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        T = len(t)
        S = len(s)
        j = 0

        if s == '':
            return True
        if S > T:
            return False

        for i in range(T):
            if s[j] == t[i]:
                if j == S - 1:
                    return True
                j += 1
        return False
        