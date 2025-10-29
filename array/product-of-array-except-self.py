class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = n-1
        left = 1
        right = 1
        l_mult = [0] * n
        r_mult = [0] * n
        for i in range(n):
            l_mult[i] = left
            r_mult[j] = right
            left *= nums[i]
            right *= nums[j]
            j -= 1
        return [l*r for l,r in zip(l_mult, r_mult)]