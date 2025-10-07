class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_done = {}
        day = 0
        for task in tasks:
            if task in last_done:
                last_day = last_done[task] + space + 1
                day = max(day+1, last_day)
            else:
                day += 1
            last_done[task] = day
        return day
