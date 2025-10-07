class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        min_i = l
        if min_i == 0:
            l, r = 0, n-1
        elif target >= nums[0] and target <= nums[min_i-1]:
            l, r = 0, min_i-1
        else:
            l, r = min_i, n-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return -1

