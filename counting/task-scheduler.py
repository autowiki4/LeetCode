class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        max_val = max(freq.values())
        max_counts = 0
        for i in freq:
            if freq[i] == max_val:
                max_counts += 1
        intervals = (max_val-1)*(n+1)+max_counts
        return max(intervals, len(tasks))
