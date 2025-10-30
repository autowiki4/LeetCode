class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0  # Total length of words (without spaces)
        
        for word in words:
            # Check if adding this word exceeds maxWidth
            # Need: current_length + len(current_line) spaces + len(word)
            if current_length + len(current_line) + len(word) > maxWidth:
                # Justify and add the current line
                result.append(self.justify_line(current_line, current_length, maxWidth, False))
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)
        
        # Handle the last line (left-justified)
        result.append(self.justify_line(current_line, current_length, maxWidth, True))
        
        return result
    
    def justify_line(self, words, length, maxWidth, is_last):
        if is_last or len(words) == 1:
            # Left-justify: single spaces between words, pad right
            return ' '.join(words).ljust(maxWidth)
        
        # Calculate spaces
        total_spaces = maxWidth - length
        gaps = len(words) - 1
        spaces_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps
        
        # Build the line
        line = []
        for i, word in enumerate(words):
            line.append(word)
            if i < gaps:  # Not the last word
                # Add base spaces + 1 extra for the first 'extra_spaces' gaps
                spaces = spaces_per_gap + (1 if i < extra_spaces else 0)
                line.append(' ' * spaces)
        
        return ''.join(line)