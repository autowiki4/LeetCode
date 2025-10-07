class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}
        def canwin(choices, remainder):
            if choices[-1]>= remainder:
                return True
            selected  = tuple(choices)
            if selected in seen:
                return seen[selected]
            for i in range(len(choices)):
                if not canwin(choices[:i]+choices[i+1:], remainder-choices[i]):
                    seen[selected] = True
                    return True
            seen[selected] = False
            return False
        
        total = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        if total < desiredTotal:
            return False
        
        if total == desiredTotal:
            return maxChoosableInteger % 2 == 1
        choice = list(range(1 , maxChoosableInteger + 1))

        return canwin(choice, desiredTotal)