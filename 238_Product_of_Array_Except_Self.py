class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        r=[]
        for i in range(len(nums)-1):
            left.append(left[-1]*nums[i])

        for i in range(len(nums)-1,0,-1):
            right.append(right[-1]*nums[i])
        right=right[::-1]
        for i in range(len(left)):
            r.append(left[i]*right[i])
        return r            
