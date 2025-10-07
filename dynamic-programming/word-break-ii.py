class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        if not dp[n]:
            return []
        
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [[]]
            if start in memo:
                return memo[start]
            
            result = []
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in wordset:
                    remaining = backtrack(end)
                    for seg in remaining:
                        result.append([word] + seg)
            memo[start] = result
            return result
        all_segments = backtrack(0)
        return[' '.join(seg) for seg in all_segments]