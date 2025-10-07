class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hour_works(hour):
            hours = 0
            for p in piles:
                hours += math.ceil(p / hour)
            
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2

            if hour_works(mid):
                r = mid
            else:
                l = mid + 1
        return r