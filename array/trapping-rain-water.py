class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i-1
            max_left[i] = l
            max_right[j] = r
            l = max(l, height[i])
            r = max(r, height[j])
        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot-height[i])
        return summ