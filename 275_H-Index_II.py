class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0
        r=len(citations)-1
        if not citations or citations[-1]==0:
            return 0
        while l<r:
            m=l+(r-l)//2
            if citations[m]>=len(citations)-m:
                r=m
            else:
                l=m+1
        return len(citations)-l
