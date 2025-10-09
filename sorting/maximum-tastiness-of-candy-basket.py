class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def can_pick(x):
            count = 1
            last = price[0]
            for p in price[1:]:
                if p-last >= x:
                    count += 1
                    last = p
                if count == k:
                    return True
            return False
        l, r = 0, price[-1]-price[0]
        while l < r:
            mid = (l+r+1) // 2
            if can_pick(mid):
                l = mid
            else:
                r=mid-1
        return l