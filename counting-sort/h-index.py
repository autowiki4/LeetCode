class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        citations = [0] + citations
        count = [i for i in range(n, 0, -1)]
        curr = 1
        for i in range(1, n+1):
            if citations[i-1] <= count[i-1]:
                curr = count[i-1]
        return curr
