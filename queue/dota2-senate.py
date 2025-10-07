class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_que = deque()
        d_que = deque()
        n = len(senate)

        for i, r in enumerate(senate):
            if r == 'R':
                r_que.append(i)
            else:
                d_que.append(i)
        while r_que and d_que:
            r_pos = r_que.popleft()
            d_pos = d_que.popleft()

            if r_pos<d_pos:
                r_que.append(r_pos+n)
            else:
                d_que.append(d_pos+n)
        return 'Radiant' if r_que else 'Dire'