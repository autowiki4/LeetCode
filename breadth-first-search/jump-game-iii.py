class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = [start]
        visited = set([start])
        while q:
            i = q.pop(0)
            if arr[i] == 0:
                return True
            l = i-arr[i]
            r = i+arr[i]
            if r < n and r not in visited:
                q.append(r)
                visited.add(r)
            if l >=0 and l not in visited:
                q.append(l)
                visited.add(l)
        return False