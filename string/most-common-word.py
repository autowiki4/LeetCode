import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        extras = set("!?',;.")
        paragraph = paragraph.lower()
        for i in paragraph:
            if i in extras:
                paragraph = paragraph.replace(i, ' ')

        words = paragraph.split()
        
        counts = defaultdict(int)
        highest_word = ''
        max_count = float('-inf')
        banned_set = set(banned)

        for word in words:
            if word not in banned_set:
                counts[word] += 1
        
        for word in words:
            if counts[word] > max_count:
                highest_word = word
                max_count = counts[word]
        return highest_word 