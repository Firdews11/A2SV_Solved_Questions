class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        num = Counter(nums)
        ans = []
        for keys,values in num.items():
            if values > n:
                ans.append(keys)
        return ans
