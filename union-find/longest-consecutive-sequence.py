class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if num-1 not in numset:
                curr = 1
                nextnum = num+1
                while nextnum in numset:
                    nextnum += 1
                    curr += 1
                longest = max(longest, curr)
        return longest