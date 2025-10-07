class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_h = 0
        curr = 0

        for h in gain:
            curr += h
            max_h = max(max_h, curr)
        return max_h