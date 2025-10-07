class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        def dfs(s, f, curr, visited):
            if s == f:
                return curr
            visited.add(s)
            for a, b in graph[s]:
                if a not in visited:
                    res = dfs(a, f, curr * b, visited)
                    if res != -1.0:
                        return res
            return -1.0

        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                ans = dfs(a, b, 1.0, set())
                result.append(ans)
        return result