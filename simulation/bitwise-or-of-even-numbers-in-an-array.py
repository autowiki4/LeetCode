class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if num % 2 == 0:
                result |= num
        return result