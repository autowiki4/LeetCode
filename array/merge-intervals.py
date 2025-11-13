class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        res = []
        curr = []
        for a, b in intervals:
            if not curr:
                curr = [a, b]
            else:
                if a > curr[-1]:
                    res.append(curr)
                    curr = [a, b]
                else:
                    curr[-1] = max(curr[-1], b)
        if curr:
            res.append(curr)
        return res