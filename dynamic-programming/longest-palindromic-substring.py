class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
    
        # Helper function to expand around the center
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
    
        for i in range(len(s)):
            # Odd length palindromes
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            
            # Even length palindromes
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
    
        return longest_palindrome