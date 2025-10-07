class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)

        right = [0] * n
        left = [0] * n
        
        j = len(nums) - 1
        for i in range(len(nums)):
            right[j] = r_mult
            left[i] = l_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
            j -= 1
        
        return [l*r for l, r in zip(left, right)]