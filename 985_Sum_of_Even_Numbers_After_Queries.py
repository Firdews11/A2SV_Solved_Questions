class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_even = sum([i for i in nums if not i %2])
        for val,index in queries:
            if not nums[index] % 2:
                sum_even -= nums[index]
            nums[index] += val
            if not nums[index] %2:
                sum_even += nums[index]
            ans.append(sum_even)
        return ans
