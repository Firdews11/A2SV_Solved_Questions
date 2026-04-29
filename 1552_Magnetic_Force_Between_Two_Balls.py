# A Binary search on the answer Q
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def feasible(d):
            count = 1
            last_pos = position[0]

            for i in range(1, len(position)):
                if position[i] - last_pos >= d:
                    count += 1
                    last_pos = position[i]

                if count >= m:
                    return True
            return False

        if m > len(position):
            return 0
        position.sort()
        l,r = 1, position[-1] - position[0]
        ans = 0
        while l<=r:
            mid = l+(r-l)//2 
            if feasible(mid):
                ans = mid
                l = mid +1
            else:
                r = mid -1
        return ans
