from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        orr, oc = entrance
        queue = deque([(orr, oc, 0)])
        visited = set()
        visited.add((orr, oc))
        
        while queue:
            r, c, curr = queue.popleft()
            if (r == 0 or r == m-1 or c == 0 or c == n-1) and (r != orr or c != oc):
                return curr 
            for a, b in [(r + 1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= a < m and 0 <= b < n and (a, b) not in visited:
                    if maze[a][b] == '.':
                        visited.add((a, b))
                        queue.append((a, b, curr + 1)) 
        
        return -1