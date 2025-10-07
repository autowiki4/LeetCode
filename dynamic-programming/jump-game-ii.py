class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr = 0
        furthest = 0
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)-1):
            if i + nums[i] >= furthest:
                furthest = i + nums[i]
            if i == curr:
                curr = furthest
                jumps += 1
        return jumps