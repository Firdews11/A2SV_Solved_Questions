class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxList = deque()
        minList = deque()
        left = 0
        answer = 0
        for right in range(len(nums)):
            x = nums[right]
            while maxList and maxList[-1] < x:
                maxList.pop()
            maxList.append(x)

            while minList and minList[-1] > x:
                minList.pop()
            minList.append(x)

            while maxList[0] - minList[0] > limit:
                y = nums[left]
                if maxList[0] == y:
                    maxList.popleft()
                if minList[0] == y:
                    minList.popleft()
                left += 1
            answer = max(answer, right - left + 1)
        return answer
