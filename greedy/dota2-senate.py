from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_que = deque()
        d_que = deque()
        n = len(senate)

        for i, v  in enumerate(senate):
            if v == 'R':
                r_que.append(i)
            else:
                d_que.append(i)
        while r_que and d_que:
            r_pos = r_que.popleft()
            l_pos = d_que.popleft()
            if r_pos < l_pos:
                r_que.append(r_pos+n)
            else:
                d_que.append(l_pos+n)
        return "Radiant" if r_que else 'Dire'