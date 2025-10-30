class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        mid = n//2
        for i in range(mid):
            words[i], words[-i-1] = words[-i-1], words[i]
        return ' '.join(words)