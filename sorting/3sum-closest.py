class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        close = float('inf')
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if abs(curr - target) < abs(close-target):
                    close = curr
                if curr == target:
                    return curr
                elif curr < target:
                    l += 1
                else:
                    r -= 1
        return close