class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        ans = 0
        
        for i in count_s:
            if count_t[i] < count_s[i]:
                ans += count_s[i] - count_t[i]
        
        return ans
