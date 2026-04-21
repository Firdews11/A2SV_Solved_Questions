class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dom = max(count, key=count.get)
        total = count[dom]
        left = 0
        n = len(nums) 
        for i in range(n):
            if nums[i] == dom:
                left += 1        
            left_size = i + 1
            right_size = n - i - 1   
            if left > left_size//2 and (total-left) > right_size//2
                return i
        return -1
