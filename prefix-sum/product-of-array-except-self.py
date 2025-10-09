class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        j = n-1
        l = [0]*n
        r = [0]*n
        for i in range(n):
            l[i] = l_mult
            r[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
            j -= 1
        return [left*right for left,right in zip(l, r)]