class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            left, right = 0, len(i)-1
            while left <= right:
                mid = (right +left)//2
                if i[mid] < 0:
                    right = mid -1
                else: 
                    left = mid +1
            count += len(i) - left
        return count
