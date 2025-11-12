class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        track = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in track:
                track[num] = []
            else:
                if abs(track[num][-1]-i) <= k:
                    return True
            track[num].append(i)
        return False