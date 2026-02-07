class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i)==1:
                return i
        # n=0
        # for i in nums:
        #     n= n^i # the sign ^ is bitwise XOR perform bits of 2 integer
        # return n
