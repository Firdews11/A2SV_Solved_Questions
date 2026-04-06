class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            l , r = 0 , len(heaters)-1
            mn = float('inf')

            while l <= r:
                m = (l+r) //2
                mn = min(mn , abs(heaters[m]-house))
                if heaters[m] < house:
                    l = m+ 1
                else:
                    r = m -1
            res = max(res, mn)
        return res
