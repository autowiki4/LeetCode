class MinStack:

    def __init__(self):
        self.stack = []
        self.prior = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prior:
            self.prior.append(min(self.prior[-1], val))
        else:
            self.prior.append(val)
        

    def pop(self) -> None:
        ans = self.stack.pop()
        self.prior.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prior[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()