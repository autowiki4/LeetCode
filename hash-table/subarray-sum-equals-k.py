class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        premap = {0:1}

        for num in nums:
            prefix += num
            if (prefix-k) in premap:
                count += premap[prefix-k]
            premap[prefix] = premap.get(prefix, 0) + 1
        return count