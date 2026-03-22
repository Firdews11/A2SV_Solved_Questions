class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        answer = [ch*count[ch] for ch in order]
        answer.extend(filter(lambda x: x not in order,s))
        return ''.join(answer)
