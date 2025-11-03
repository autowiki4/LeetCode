class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        curr = 0
        min_len = float('inf')
        for r in range(n):
            curr += nums[r]
            while curr >= target:
                min_len = min(min_len, r-l+1)
                curr -= nums[l]
                l += 1
        return min_len if min_len < float('inf') else 0
