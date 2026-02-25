class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while a <= b:
            sqr = a**2 + b**2
            if sqr == c:
                return True
            elif sqr > c:
                b -=1
            else:
                a +=1
        return False
