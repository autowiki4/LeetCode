class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        result = []
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]