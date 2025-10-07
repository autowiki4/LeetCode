class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        current_range = ''

        for i in range(len(nums)):
            if i == len(nums) - 1:
                if current_range:
                    current_range += str(nums[i])
                    ranges.append(current_range)
                else:
                    ranges.append(str(nums[i]))
            else:
                if not current_range:
                    if nums[i+1] == nums[i] + 1:
                        current_range = f'{nums[i]}->'
                    else:
                        ranges.append(str(nums[i]))
                else:
                    if nums[i+1] != nums[i] + 1:
                        current_range += str(nums[i])
                        ranges.append(current_range)
                        current_range = ''
        
        return ranges