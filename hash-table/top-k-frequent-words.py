import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        
        heap = []
        heapq.heapify(heap)
        for word, freq in counts.items():
            heapq.heappush(heap, (-freq, word))
        
        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result