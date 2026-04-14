class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {value: occ for occ, value in enumerate(s)}
        res = []
        start = 0
        end = 0
        for i , value in enumerate(s):
            end = max(end,last_occ[value])
            if i == end:
                res.append(end -start +1)
                start = i+1
        return res
