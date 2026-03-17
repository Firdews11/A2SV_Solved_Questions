class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                check = stack.pop()
                if check == 0:
                     stack[-1] += 1
                else:
                    stack[-1] += (check * 2)   
        return stack[0]
