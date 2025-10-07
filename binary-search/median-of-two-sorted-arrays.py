class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_list = nums1 + nums2
        # for item in nums1:
        #     combined_list.append(item)
        # for item in nums2:
        #     combined_list.append(item)
        # arrange the list in ascending order
        combined_list.sort()
        no_items = len(combined_list)
        if no_items % 2 == 0:
            return (combined_list[-1+(int(no_items/2))]+combined_list[-1+(int(no_items/2)+1)]) / 2
        elif no_items % 2 == 1:
            return combined_list[-1+(int(no_items/2)+1)]