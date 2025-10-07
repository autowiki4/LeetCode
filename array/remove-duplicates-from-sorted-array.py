class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        curr = nums[0]
        for r in range(len(nums)):
            if nums[r] != curr:
                curr = nums[r]
                nums[l] = nums[r]
                l += 1
        return l
        