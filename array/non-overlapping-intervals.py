class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count = 1
        end = intervals[0][1]
        for interval in intervals:
            if interval[0] >= end:
                count += 1
                end = interval[1]
        return len(intervals) - count