class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        track = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in track:
                if abs(track[num]-i) <= k:
                    return True
            track[num] = i
        return False