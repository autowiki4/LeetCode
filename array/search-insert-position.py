class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if not low:
            if nums[low] > target:
                return 0
            elif nums[low] < target:
                return low + 1
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
        