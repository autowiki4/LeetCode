class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words_list = s.split()
        words_list = words_list[::-1]

        output = ' '.join(words_list)
        return output