class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in rem:
                return [rem[num], i]
            rem[target-num] = i