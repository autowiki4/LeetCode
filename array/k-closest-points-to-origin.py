import heapq
import math
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance (x, y):
            return sqrt(x**2 + y**2)
        
        heap = []
        heapq.heapify(heap)

        for x,y in points:
            d = distance(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else:
                heapq.heappushpop(heap, (-d, x, y))
        
        return [(x,y) for d,x,y in heap]