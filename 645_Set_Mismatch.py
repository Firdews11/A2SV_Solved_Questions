class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n =len(nums)
        s = sum(set(nums))
        m = n * (n+1)//2
        n_sum = sum(nums)
        return [n_sum - s, m-s]
