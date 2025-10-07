class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        order = []

        for a, b in prerequisites:
            graph[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]

            if state == VISITED:
                return True
            if state == VISITING:
                return False
            
            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order