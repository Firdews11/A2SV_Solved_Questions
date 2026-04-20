from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        seen = SortedList() 
        ans = []
        for i in nums[::-1]:
            position = seen.bisect_left(i)
            ans.append(position)
            seen.add(i)
        return ans[::-1]
