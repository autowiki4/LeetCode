class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = 0
        for i in nums:
            curr ^= i
        return curr