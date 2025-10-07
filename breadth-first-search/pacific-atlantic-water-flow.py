from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        m, n  = len(heights), len(heights[0])

        for i in range(n):
            p_que.append((0, i))
            p_seen.add((0, i))
        
        for j in range(1, m):
            p_que.append((j, 0))
            p_seen.add((j, 0))
        
        for i in range(n):
            a_que.append((m - 1, i))
            a_seen.add((m-1, i))
        
        for j in range(m - 1):
            a_que.append((j, n-1))
            a_seen.add((j, n-1))
        
        def seen_set(que, seen):
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    if 0<=r<m and 0<=c<n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
        seen_set(p_que, p_seen)
        seen_set(a_que, a_seen)
        return list(p_seen.intersection(a_seen))