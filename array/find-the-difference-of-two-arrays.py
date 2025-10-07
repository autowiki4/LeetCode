class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        ans1 = []
        ans2 = []
        for i in set(nums1):
            if i not in set(nums2):
                ans1.append(i)
        for i in set(nums2):
            if i not in set(nums1):
                ans2.append(i)
        ans.append(ans1)
        ans.append(ans2)
        return ans       