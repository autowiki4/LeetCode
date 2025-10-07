class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0
        r = 0
        while r < len(chars):
            char = chars[r]
            c = 0
            while r < len(chars) and chars[r] == char:
                r += 1
                c += 1
            chars[w] = char
            w += 1
            if c > 1:
                for d in str(c):
                    chars[w] = d
                    w += 1
        return w