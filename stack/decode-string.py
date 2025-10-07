class Solution:
    def decodeString(self, s: str) -> str:
        digits = []
        strings = []
        curr_num = 0
        curr_str = ''

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                digits.append(curr_num)
                strings.append(curr_str)
                curr_num = 0
                curr_str = ''
            elif c == ']':
                rep = digits.pop()
                prev = strings.pop()
                curr_str = prev + curr_str*rep
            else:
                curr_str += c
        return curr_str
            
        