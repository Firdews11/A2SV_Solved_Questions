class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = defaultdict(lambda: -1)
        for num in nums2:
            while stack and num > stack[-1]:
                removed_val = stack.pop()
                dic[removed_val] = num
            stack.append(num)
        return [dic[num] for num in nums1]
