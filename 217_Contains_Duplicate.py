class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
        # n = set(nums)
        # if len(n)!=len(nums):
        #     return True
        # return False
