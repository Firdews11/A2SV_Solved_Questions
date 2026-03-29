class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shifting = [0] * (n + 1) 
        for start, end, direction in shifts:
            if direction == 1:
                shift_to = 1 
            else:
                shift_to = -1
            shifting[start] += shift_to
            if end + 1 < n:
                shifting[end + 1] -= shift_to
                
        total_shift = [0] * n
        pri = 0
        for i in range(n):
            pri += shifting[i]
            total_shift[i] = pri
        s= list(s) 
    
        for i in range(n):
            char = ord(s[i]) - ord('a')

            new = (char + total_shift[i]) % 26
            
            s[i] = chr(new + ord('a'))
        return "".join(s)
