class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0
        x = max(candies)
        l, r = 1, x
        while l <=r:
            mid = l+(r-l)//2 
            total = sum([i//mid for i in candies])
            if total >=k:
                l = mid +1
            else:
                r = mid -1
        return r
