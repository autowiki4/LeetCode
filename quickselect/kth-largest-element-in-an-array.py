import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        i = 0
        heapq.heapify(nums)
        while i < k:
            curr = heapq.heappop(nums)
            i += 1
        return -curr