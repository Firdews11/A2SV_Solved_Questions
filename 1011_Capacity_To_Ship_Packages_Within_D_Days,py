class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # capacity is the mid
        def check(capacity , weight):
            day = 1
            curr_sum = 0
            for w in weights:
                if w +curr_sum > capacity:
                    day +=1
                    curr_sum = w
                else:
                    curr_sum +=w
            return day <= days

        l = max(weights)
        r = sum(weights)
        ans = -1
        while l <=r:
            mid = (r+l) //2
            if check(mid,weights):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
