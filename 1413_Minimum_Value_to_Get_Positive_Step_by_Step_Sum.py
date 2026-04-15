class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        #[0,-3,-1,-4,0,2]
        return(max(1,1-min(nums)))
