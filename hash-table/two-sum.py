class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        sum_dict = {}
        for i,num in enumerate(self.nums):
            diff = self.target - num
            if diff in sum_dict:
                return [sum_dict[diff], i]
            else:
                sum_dict[num] = i 

test_case = Solution()
print(test_case.twoSum(nums=[2,7,11,15], target = 9))


        