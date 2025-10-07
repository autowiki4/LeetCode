class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        
        wordset = set(wordDict)
        max_len = max(len(word) for word in wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n+1):
            for j in range(max(0, i-max_len), i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]