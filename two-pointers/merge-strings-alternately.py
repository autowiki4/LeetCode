class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = len(min([word1, word2], key=len))
        merged_word = ''
        for index in range(min_length):
            merged_word += word1[index] + word2[index]
        
        if word1[min_length:]:
            merged_word += word1[min_length:]
        else:
            merged_word += word2[min_length:]
        
        return merged_word