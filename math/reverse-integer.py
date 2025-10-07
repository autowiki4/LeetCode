class Solution:
    def reverse(self, x: int) -> int:
        no_str = str(x)
        rev = no_str[1:][::-1] if no_str[0] == '-' else no_str[::-1]
        output = int(rev) if no_str[0] != '-' else int(f'-{rev}')
        check = output>=-2**31 and output <= 2**31-1
        return output if check else 0
        