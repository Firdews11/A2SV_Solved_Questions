class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        c = sorted(count.items(), key= lambda item: item[1], reverse=True)
        return ''.join(key*values for key,values in c)
