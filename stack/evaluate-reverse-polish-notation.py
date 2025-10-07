class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                current = stack[-2] + stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(current)
            elif token == '-':
                current = stack[-2] - stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(current)
            elif token == '*':
                current = stack[-2] * stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(current)
            elif token == '/':
                current = int(stack[-2] / stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(current)
            else:
                stack.append(int(token))
        
        return stack[0]