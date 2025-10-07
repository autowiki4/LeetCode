class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a,b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        reorder = 0
        def dfs(node, parent):
            nonlocal reorder
            for nei, order in graph[node]:
                if nei == parent:
                    continue
                reorder += order
                dfs(nei, node)
        dfs(0, -1)
        return reorder
