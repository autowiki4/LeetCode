class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while True:
            curr = 0
            for d in str(n):
                num = int(d)
                curr += num**2
            if curr in cycle:
                return False
            if curr == 1:
                return True
            cycle.add(curr)
            n = curr
            