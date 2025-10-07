class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        mid = n // 2
        for num in count:
            if count[num] > mid:
                return num
        