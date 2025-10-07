class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        roman_to_num = 0
        for i in range(len(s) - 1):
            if roman_num[s[i]] < roman_num[s[i+1]]:
                    roman_to_num -= roman_num[s[i]]
            else:
                roman_to_num += roman_num[s[i]]
        roman_to_num += roman_num[s[-1]]
        return roman_to_num 
        