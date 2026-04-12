class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        joined= [item for sublist in matrix for item in sublist]
        
        l=0
        r=len(joined)-1
        while l<=r:
            m= (l+r)//2
            if joined[m]> target:
                r=m-1
            elif joined[m]<target:
                l=m+1
            else:
                return True
        return False        
