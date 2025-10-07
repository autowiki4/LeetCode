import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        tester = stones

        for i in range(len(stones)):
            tester[i] = -tester[i]
        
        heapq.heapify(tester)

        while len(tester) > 1:
            min1 = heapq.heappop(tester)
            min2 = heapq.heappop(tester)

            if min1 != min2:
                heapq.heappush(tester, min1 - min2)
        if tester:
            return -tester[0]
        return 0
