import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.next = 1
        self.heap = []
        self.added = set()

    def popSmallest(self) -> int:
        if self.heap and self.heap[0] < self.next:
            small = heapq.heappop(self.heap)
            self.added.remove(small)
            return small
        else:
            small = self.next
            self.next += 1
            return small

    def addBack(self, num: int) -> None:
        if num < self.next and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)