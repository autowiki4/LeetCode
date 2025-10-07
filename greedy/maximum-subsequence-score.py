import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        pairs.sort(key=lambda x :x[1], reverse=True)

        curr = 0
        max_score = 0
        heap = []

        for num1, num2 in pairs:
            heapq.heappush(heap, num1)
            curr += num1
            if len(heap) > k:
                removed = heapq.heappop(heap)
                curr -= removed
            if len(heap) == k:
                score = curr * num2
                max_score = max(max_score, score)
        return max_score