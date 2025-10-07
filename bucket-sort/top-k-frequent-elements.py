from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        frequency = []
        heapq.heapify(frequency)

        for num, count in counter.items():
            heapq.heappush(frequency, (-count,num))
        
        output = []

        for _ in range(k):
            output.append(heapq.heappop(frequency)[1])
        
        return output