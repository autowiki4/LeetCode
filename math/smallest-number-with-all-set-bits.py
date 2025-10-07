import math
class Solution:
    def smallestNumber(self, n: int) -> int:
        nearest = math.floor(math.log2(n)) + 1
        return 2 ** nearest - 1