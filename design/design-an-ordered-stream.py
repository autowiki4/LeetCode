class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n+1)
        self.id = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []
        while self.id < len(self.stream) and self.stream[self.id] is not None:
            result.append(self.stream[self.id])
            self.id += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)