class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        for a, b in roads:
            count[a] += 1
            count[b] += 1
        
        # Sort cities by number of connections
        sorted_cities = sorted(range(n), key=lambda i: count[i])
        
        # Assign importance values
        importance = [0] * n
        for i in range(n):
            importance[sorted_cities[i]] = i + 1
        
        # Calculate total importance
        total = 0
        for a, b in roads:
            total += importance[a] + importance[b]
        
        return total