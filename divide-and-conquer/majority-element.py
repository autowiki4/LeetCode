class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        mid = int(len(nums)/2)
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > mid:
                return num