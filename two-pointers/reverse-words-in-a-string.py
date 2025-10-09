class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        mid = n//2
        for i in range(mid):
            words[i], words[n-i-1] = words[n-i-1], words[i]
        return ' '.join(words)
        