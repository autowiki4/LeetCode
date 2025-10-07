class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        curr = 0
        vow_set = {'a', 'e', 'i', 'o', 'u'}

        for i in range(k):
            if s[i] in vow_set:
                curr += 1
        max_vow = curr
        
        for i in range(k, n):
            if s[i-k] in vow_set:
                curr -= 1
            if s[i] in vow_set:
                curr += 1
            print(curr)
            max_vow = max(max_vow, curr)
        return max_vow