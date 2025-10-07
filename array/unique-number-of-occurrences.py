class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        return len(set(count.values())) == len(set(count.keys()))