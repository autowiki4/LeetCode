class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if max_area < min(height[right], height[left]) * abs(right-left):
                max_area = min(height[right], height[left]) * abs(right-left)
            if height[right] < height[left]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return max_area
        