class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        curr = max(nums[0], nums[1])
        n = len(nums)

        for i in range(2, n):
            prev, curr = curr, max(prev+nums[i], curr)
        return curr