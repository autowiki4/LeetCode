from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = defaultdict(list)
        ans = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in ans:
                ans[key] = []
            ans[key].append(s)
        
        return list(ans.values())