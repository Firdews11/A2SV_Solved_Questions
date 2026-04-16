from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
# so we can take some ideas from Q 2426. Number of Pairs Satisfying Inequality

# so we the Q is asking to insert the current number into a sorted arr but befor insertion we compute a cost the cost is basically: 
         # min( how many numbers < x, how many numbers > x)
# using bisect_left we can get number of the numbers that are less than < x  and using bisect_right we get less than or equal to <=, but to get strictly greater than x we need to subrtact bisect_right from the size of arr itself soo the code will be:
# les = arr.bisect_left(x)
# less_or equal = arr.bisect_right(x)
# greater = len(arr) - less_or equal
# cost = min(less,greater)
# then u add x at the sorted arr

        arr =SortedList()
        cost = 0
        mod = 10**9 + 7

        for x in instructions:
            less = arr.bisect_left(x)
            less_or_equal = arr.bisect_right(x)
            greater = len(arr) - less_or_equal
            cost += min(less,greater)
            cost %= mod
            arr.add(x)
        return cost
