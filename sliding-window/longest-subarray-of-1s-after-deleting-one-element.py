class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        max_w = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            curr = r-l
            max_w = max(max_w, curr)
        return max_w
