class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if not words or not chars:
            return 0
        length = 0
        chars_count = Counter(chars)

        for word in words:
            word_count = Counter(word)  
            x = True
            for letter, count in word_count.items():
                if count > chars_count.get(letter, 0):
                    x = False
                    break
            if x:
                length += len(word)

        return length
