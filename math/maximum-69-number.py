class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = str(num)
        n  = len(digits)
        maximum = num
        def change(i):
            if digits[i] == '6':
                return digits[:i] + '9' + digits[i+1:]
            return digits[:i] + '6' + digits[i+1:]
        
        for i in range(n):
            new = int(change(i))
            maximum = max(maximum, new)
        return maximum