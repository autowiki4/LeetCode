class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        overlap = []

        for interval in intervals:
            if not overlap or overlap[-1][1] < interval[0]:
                overlap.append(interval)
            else:
                overlap[-1] = [overlap[-1][0], max(overlap[-1][1], interval[1])]
        
        return overlap