class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        rem = n-k
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        if k > 0:
            stack = stack[:rem]
        if len(stack) == 0:
            return '0'
        j = 0
        while j < len(stack) and stack[j] == '0':
            j += 1
        stack = stack[j:]
        return ''.join(stack) if stack else '0'
