class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = list(s.split())
        if len(words) != len(pattern):
            return False
        wp = {}
        pw = {}
        for i in range(len(words)):
            wc = words[i]
            pc = pattern[i]
            if wc in wp:
                if wp[wc] != pc:
                    return False
            else:
                wp[wc] = pc
            if pc in pw:
                if pw[pc] != wc:
                    return False
            else:
                pw[pc] = wc
        return True
        