class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        #solution 1
        # if len(nums) <2:
        #     return 0
        # min_val =min(nums)
        # max_val = max(nums)
        # n = len(nums)
        # #the numbers inside nums might be all equal sooo..
        # if min_val == max_val:
        #     return 0
        # #lets see, our bucket size gotta be 
        # b_size = max(1,(max_val-min_val)// (n-1))
        # bucket_count = (max_val - min_val) // b_size + 1 # we did + 1 b/c when we use // it rounds down
        # b_min = [float("inf")]* bucket_count
        # b_max = [float ("-inf")]* bucket_count
        # for i in nums:
        #     idx = (i - min_val)//b_size
        #     b_min[idx] = min(b_min[idx] , i)
        #     b_max[idx] = max(b_max[idx], i)

        # max_gap = 0
        # prev_max = min_val

        # for i in range(bucket_count):
        #     if b_min[i] == float('inf'):
        #         continue
        #     max_gap = max(max_gap, b_min[i] - prev_max)
        #     prev_max = b_max[i]
        # return max_gap


        #solution 2
        if len(nums) < 2:
            return 0
        nums = sorted(set(nums))
        max_gap = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            gap = nums[i] - prev
            max_gap = max(max_gap, gap)
            prev = nums[i]

        return max_gap
