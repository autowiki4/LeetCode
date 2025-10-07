class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # Build adjacency set for quick lookup
        graph = [set() for _ in range(n + 1)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # Find nodes with odd degrees
        odd_nodes = [i for i in range(1, n + 1) if len(graph[i]) % 2 == 1]
        
        # Case 1: No odd-degree nodes
        if not odd_nodes:
            return True
        
        # Case 2: Two odd-degree nodes
        if len(odd_nodes) == 2:
            u, v = odd_nodes
            # Can connect them directly if no edge exists
            if v not in graph[u]:
                return True
            
            # Or connect each to a third node if possible
            for i in range(1, n + 1):
                if i != u and i != v and i not in graph[u] and i not in graph[v]:
                    return True
            return False
        
        # Case 3: Four odd-degree nodes
        if len(odd_nodes) == 4:
            a, b, c, d = odd_nodes
            # Check all possible ways to add 2 edges
            return (b not in graph[a] and d not in graph[c]) or \
                (c not in graph[a] and d not in graph[b]) or \
                (d not in graph[a] and c not in graph[b])
        
        # Case 4: More than 4 odd-degree nodes - impossible
        return False