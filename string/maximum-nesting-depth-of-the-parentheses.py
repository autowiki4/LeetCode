class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        i = 0
        n = len(s)
        open_br = '('
        close = ')'
        curr = 0
        for c in s:
            if c == open_br:
                curr += 1
            elif c == close:
                curr -= 1
            max_depth = max(curr, max_depth)
        return max_depth