class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = [word[::-1] for word in s.split()]
        reverse_s = ' '.join(word_list)
        return reverse_s
