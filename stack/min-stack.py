class MinStack:

    def __init__(self):
        self.stk = []
        self.track= []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.track:
            self.track.append(val)
        else:
            if val <= self.track[-1]:
                self.track.append(val)
            else:
                temp = self.track.pop()
                self.track.append(val)
                self.track.append(temp)

    def pop(self) -> None:
        last = self.stk.pop()
        if self.track[-1] == last:
            self.track.pop()


    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.track[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()