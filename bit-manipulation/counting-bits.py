class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0, 1]
        curr = 1
        epsilon = 1e-10
        for i in range(2, n+1):
            if curr*2 == i:
                curr = i
                memo.append(1)
            else:
                left = i - curr
                add = memo[curr] + memo[left]
                memo.append(add)
        return memo[:n+1]       