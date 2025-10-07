class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        n, m = len(spells), len(potions)
        for i in range(n):
            spell = spells[i]
            l, r = 0, m - 1
            left = m
            while l <= r:
                mid = (l+r) // 2
                curr = spell * potions[mid]
                if curr >= success:
                    left = mid
                    r = mid - 1
                else:
                    l = mid + 1
            pairs.append(m-left)
        return pairs



        