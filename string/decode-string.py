class Solution:
    def decodeString(self, s: str) -> str:
        seq = []
        digits = []
        num = 0
        curr = ''

        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                digits.append(num)
                seq.append(curr)
                curr = ''
                num = 0
            elif c == ']':
                number = digits.pop()
                prev = seq.pop()
                curr = prev + curr*number
            else:
                curr += c
        return curr
