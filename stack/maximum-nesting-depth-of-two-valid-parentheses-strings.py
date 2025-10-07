class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        answer = []
        curr = 0
        for c in seq:
            if c == '(':
                curr += 1
                answer.append(curr % 2)
            elif c == ')':
                answer.append(curr%2)
                curr -= 1
        return answer