from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
        # nums1[i] - nums2[i] <= nums1[j] - nums2[j] + dif


#nums1 = [3, 2, 5]
#nums2 = [2, 2, 1]
#diff = 1

#we will have:

#count = 0
#arr = [1,0,4] ## which is nums1[i] - nums2[i] part
#lets assign a sorted list s_l = [ ]
# and we are supposed to find how many numbers there are that are:
            # 0 <= i < j <= n - 1  and
            # nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff

# what if we say " nums1[i] - nums2[i] " this part is arr[i] and
# " nums1[j] - nums2[j] " arr[j] so the eqation becames arr[i] <= arr[j] + diff
# what if we say arr[j] is the limit and the equation arr[i]+ diff >= arr[j]


#our itration become 

# 1st itration
# limit = arr[i] + diff -> 1 + 1 =2 , now the checking becomes How many numbers are in sl that are <= 2? w/c is none, then we add arr[i] into the sl

#2nd itration
#limit = arr[i] + diff -> 0 + 1 =1 again How many numbers are in sl that are <= 1? now the answer is 1 so our count increase by 1 count +=1, and also add the arr[i] to sl

#3rd itration
#limit = arr[i] + diff -> 4 + 1 = 5, How many numbers are in sl that are <= 5, there are 2, so our count will be count +=2 increase by 2, and then add it to sl 

### now for checking the condition "How many numbers are in sl that are <= some number" we can use .bisect_right(some number)
        
    
        sl = SortedList()
        count = 0

        for i in range(len(nums1)):
            val = nums1[i] - nums2[i]
            limit = val + diff
            count += sl.bisect_right(limit)
            sl.add(val)

        return count
