import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if 2 * candidates >= n:
            costs.sort()
            return sum(costs[:k])
        l_heap = []
        r_heap = []
        for i in range(candidates):
            heapq.heappush(l_heap, costs[i])
        for i in range(n-candidates, n):
            heapq.heappush(r_heap, costs[i])
        l = candidates
        r = n- candidates - 1
        total_cost = 0
        for _ in range(k):
            l_min = l_heap[0] if l_heap else float('inf')
            r_min = r_heap[0] if r_heap else float('inf')
            if l_min <= r_min:
                cost = heapq.heappop(l_heap)
                total_cost += cost
                if l <= r:
                    heapq.heappush(l_heap, costs[l])
                    l += 1
            else:
                cost = heapq.heappop(r_heap)
                total_cost += cost
                if l <= r:
                    heapq.heappush(r_heap, costs[r])
                    r -= 1
        return total_cost
        