class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Build the graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize data structures
        disc = [-1] * n  # Discovery times
        low = [-1] * n   # Lowest reachable node
        visited = [False] * n
        result = []
        self.time = 0
        
        def dfs(u, parent):
            self.time += 1
            disc[u] = low[u] = self.time
            visited[u] = True
            
            for v in graph[u]:
                if v == parent:
                    continue  # Skip the parent node
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        result.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])
        
        # Start DFS from node 0
        dfs(0, -1)
        return result  