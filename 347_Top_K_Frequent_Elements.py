class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count.items(), key= lambda x:x[1],reverse = True)
        ans = [sorted_count[i][0] for i in range(k)]
        return ans
