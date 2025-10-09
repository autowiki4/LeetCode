class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        oper = 0
        for num in nums:
            comp = k - num
            if comp in count and count[comp] > 0:
                count[comp] -= 1
                oper += 1
                if count[comp] == 0:
                    del count[comp]
            else:
                count[num] = count.get(num, 0) + 1
        return oper