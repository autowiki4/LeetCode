class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        citations = [0] + citations
        count = [i for i in range(n, -1, -1)]
        curr = 0
        for i in range(n+1):
            if citations[i] <= count[i]:
                curr = count[i]
        return curr
