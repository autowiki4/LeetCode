class Solution:
    def removeStars(self, s: str) -> str:
        chars = []
        for c in s:
            if c.isalpha():
                chars.append(c)
            else:
                chars.pop()
        return ''.join(chars)