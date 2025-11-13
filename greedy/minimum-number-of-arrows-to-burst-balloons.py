class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[0])
        curr = -float('inf')
        arrows = 0

        for a,b in points:
            if a > curr:
                arrows += 1
                curr = b
            else:
                curr = min(curr, b)
        return arrows
            