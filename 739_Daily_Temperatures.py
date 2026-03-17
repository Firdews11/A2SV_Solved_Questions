class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ans =[0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[i] >temp[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day]= i - prev_day
            stack.append(i)
        return ans
