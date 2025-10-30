class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = min([len(word) for word in strs])

        prefix = ''
        for i in range(longest):
            check = set()
            for word in strs:
                check.add(word[i])
            if len(check) > 1:
                return prefix
            prefix += check.pop()
        return prefix
