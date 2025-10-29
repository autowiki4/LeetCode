class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = 0
        index = 0
        n = len(cost)
        for i in range(n):
            if gas[i] > cost[i]:
                index = i
                curr = gas[i] - cost[i]
                break
            if i == n-1:
                return -1
        i = (index + 1) % n
        curr += gas[i]
        while True:
            if i == index:
                return index
            if curr < cost[i]:
                return -1
            curr -= cost[i]
            nxt = (i+1) % n
            curr += gas[nxt]
            i = nxt
        


            