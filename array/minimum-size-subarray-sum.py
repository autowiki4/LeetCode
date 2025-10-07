class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        minimum_length = float('inf')

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                minimum_length = min(minimum_length, r-l+1)
                summ -= nums[l]
                l += 1
        return minimum_length if minimum_length < float('inf') else 0