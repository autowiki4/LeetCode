from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        q = deque()
        fresh = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            rotting = len(q)
            for _ in range(rotting):
                i, j = q.popleft()
                for r, c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r, c))
            minute +=1
        return minute if fresh == 0 else -1