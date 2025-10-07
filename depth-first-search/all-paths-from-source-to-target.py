class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)
        def dfs(i, curr):
            if i == n-1:
                result.append(curr[:])
                return
            for node in graph[i]:
                curr.append(node)
                dfs(node, curr)
                curr.pop()
        dfs(0, [0])
        return result