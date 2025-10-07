from collections import defaultdict
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i,p in enumerate(parent):
            graph[p].append(i)
        
        ans = 1
        def dfs(node):
            nonlocal ans
            longest = sec_long = 0

            for c in graph[node]:
                path = dfs(c)
                if s[c] != s[node]:
                    if path > longest:
                        sec_long = longest
                        longest = path
                    elif path > sec_long:
                        sec_long = path
            ans = max(ans, longest + sec_long + 1)
            return longest + 1
        dfs(0)
        return ans