class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #first lets make sure we are serching for the smallest array length if we dont we might get a negative num when doing the cuts
        if len(nums1) >len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1) , len(nums2)
        l,r = 0, m -1
        total = m +n
        half = total//2
        while True:
            c1 = (l+r)//2 # the cut for num1
            c2 = half - c1 -2 # the cut for num2, so our left side cut is the sum of c1 and c2
            n1_left = nums1[c1] if c1 >= 0 else float("-inf")
            n1_right = nums1[c1+1] if (c1 +1) < m else float("inf")
            n2_left = nums2[c2] if c2 >= 0 else float("-inf")
            n2_right = nums2[c2+1] if (c2 +1) < n else float("inf")

            if n1_left <= n2_right and n2_left <= n1_right:
                #tho if sum of the 2 arrays is odd
                if total % 2:
                    return (min(n1_right,n2_right))
                #if its even
                return (max(n1_left,n2_left) + min(n1_right,n2_right)) /2 #we will be needing a decimal number here
            elif n1_left > n2_right:
                r = c1 - 1
            else:
                l = c1 + 1
