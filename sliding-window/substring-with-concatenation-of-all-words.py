class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        # Create frequency map of words
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        result = []
        
        # Only need to check word_len different starting positions
        for i in range(word_len):
            left = i
            right = i
            current_freq = {}
            count = 0
            
            while right + word_len <= len(s):
                # Add word from right
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    current_freq[word] = current_freq.get(word, 0) + 1
                    count += 1
                    
                    # If word appears too many times, shrink window
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # Check if we found a valid substring
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset if word not in list
                    current_freq.clear()
                    count = 0
                    left = right
        
        return result