class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
    
    def move(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        


    def pop(self) -> int:
        self.move()
        return self.output.pop()


    def peek(self) -> int:
        self.move()
        return self.output[-1]


    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()