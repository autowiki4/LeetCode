class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def check_zero(num):
            digits = str(num)
            for dig in digits:
                if dig == '0':
                    return False
            return True
        
        for i in range(n):
            check = i
            checker = n - i
            if check_zero(check) and check_zero(checker):
                return [check, checker]