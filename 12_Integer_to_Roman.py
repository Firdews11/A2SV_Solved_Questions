class Solution:
    def intToRoman(self, num: int) -> str:
#  num = 3749
# 3749 >= 1000 -> r= "M
# 2749 >= 1000 -> r= "MM
# 1749 >= 1000 -> r= "MMM
# 749  >= 500  -> r="MMMD
#   749- 500 = 249
# 249 >= 100 -> r="MMMDC
# 149 >= 100 -> r="MMMDCC
# 49 >= 40 ->r="MMMDCCXL
# 9 >= 9 ->  r= ""MMMDCCXLIX""
        values = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),
                (90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),
                (4, "IV"),(1, "I")]

        res = ""

        for val, roman in values:
            while num >= val:
                res += roman
                num -= val

        return res
