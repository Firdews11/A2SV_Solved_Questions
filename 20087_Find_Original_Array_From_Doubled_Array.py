class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) %2 != 0 :
            return []
        if 0 in changed and changed.count(0) %2 !=0:
            return []
        changed.sort()
        chenged_count = Counter(changed)
        ans = []
        for i in changed:
            if chenged_count[i] == 0:
                continue 
            if chenged_count[i*2] == 0:
                return []
            else:
                ans.append(i)
                chenged_count[i] -=1
                chenged_count[i*2] -=1
        return ans
