class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in str:
            key = tuple(sorted(s))
            if key not in ans:
                ans[key] = []
            ans[key].append(s)
        return list(ans.values())