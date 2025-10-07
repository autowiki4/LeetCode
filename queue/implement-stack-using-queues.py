from collections import deque
class MyStack:

    def __init__(self):
        self.input = deque()

    def push(self, x: int) -> None:
        self.input.append(x)
        for _ in range(len(self.input)-1):
            self.input.append(self.input.popleft())

    def pop(self) -> int:
        return self.input.popleft()

    def top(self) -> int:
        return self.input[0]

    def empty(self) -> bool:
        return len(self.input) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()