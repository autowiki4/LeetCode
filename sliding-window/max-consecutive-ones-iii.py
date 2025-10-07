class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_width = 0
        num_zero = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            width = r-l+1
            max_width = max(width, max_width)
        return max_width