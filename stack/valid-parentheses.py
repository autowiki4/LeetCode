class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in brackets:
                stack.append(c)
            elif not stack:
                return False
            else:
                if brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return True if not stack else False