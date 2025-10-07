class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid = 0
        ln = len(flowerbed)
        for i in range(ln):
            if flowerbed[i]==0 and (i == 0 or flowerbed[i-1] == 0) and (i==ln-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                valid += 1
                if valid >= n:
                    return True
        return valid >= n