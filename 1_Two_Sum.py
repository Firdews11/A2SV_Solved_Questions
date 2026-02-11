class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m_p={}
        for i ,j in enumerate(nums):
            x = target-j
            if x in m_p:
                return[m_p[x],i]
            m_p[j] = i  
