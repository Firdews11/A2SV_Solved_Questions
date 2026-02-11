class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {"I":1 , "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        prev_num = 0
        for i in s[::-1]:
                if roman_num[i] < prev_num:
                    total -= roman_num[i]
                else:
                    total += roman_num[i]
                prev_num = roman_num[i]
            
        return total
