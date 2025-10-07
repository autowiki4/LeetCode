class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        greatest = [candy + extraCandies >= max_candy for candy in candies]
        return greatest                