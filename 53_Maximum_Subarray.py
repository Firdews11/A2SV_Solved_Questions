class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        max_ = nums[0]

        for i in range(len(nums)):
            current += nums[i]
            if current > max_:
                max_ = current
               
            if current < 0:
                current = 0

        return max_
