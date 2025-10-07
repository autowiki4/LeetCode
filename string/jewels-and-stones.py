class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)

        output = 0
        for stone in stones:
            if stone in jewel_set:
                output += 1
        
        return output