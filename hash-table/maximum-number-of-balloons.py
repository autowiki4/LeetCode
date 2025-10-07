class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_chars = set('balloon')
        balloon_count = {}
        
        for char in 'balloon':
            balloon_count[char] = balloon_count.get(char, 0) + 1
        
        balloon_words = {}
        for char in text:
            if char in balloon_chars:
                balloon_words[char] = balloon_words.get(char, 0) + 1
        
        char_nums = {}

        for char in balloon_count:
            text_count = balloon_words.get(char, 0)
            char_nums[char] = int(text_count / balloon_count[char])
        
        return min(char_nums.values())