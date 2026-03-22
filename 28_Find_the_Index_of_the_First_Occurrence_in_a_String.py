class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        if needle not in haystack:
            return -1

        for i in range(len(haystack) - n + 1):
            if haystack[i:n+i] == needle:
                return i
