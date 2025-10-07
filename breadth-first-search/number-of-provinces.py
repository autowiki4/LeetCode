from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        prov = 0

        def dfs(city):
            visited.add(city)
            for nei in range(n):
                if isConnected[city][nei] and nei not in visited:
                    dfs(nei)
        for city in range(n):
            if city not in visited:
                dfs(city)
                prov += 1
        return prov

                

        