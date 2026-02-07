class Solution:
    def checkEqual(self, a, b) -> bool:
        a = sorted(a)
        b = sorted(b)
        return a == b
