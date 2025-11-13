class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        files = path.split('/')
        for f in files:
            if f == '.':
                pass
            elif f == '..':
                if stack:
                    stack.pop()
            elif f:
                stack.append(f)
        return '/' + '/'.join(stack)