class Solution:
    def isPalindrome(self, x: int) -> bool:
        no_string = str(x)
        output = ''
        index = 1
        while index <= len(no_string):
            output += no_string[-index]
            index += 1
        return output == no_string
        