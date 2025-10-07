class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap, weights, days):
            d = 1
            curr = 0
            for w in weights:
                if curr + w > cap:
                    d += 1
                    curr = w
                else:
                    curr += w
            return d <= days
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l+r) // 2
            if canShip(mid, weights, days):
                r = mid
            else:
                l = mid + 1
        return l