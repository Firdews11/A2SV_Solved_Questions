class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            if stack[-1] == "*":
                stack.pop()
                stack.pop()
        return ''.join(stack)
