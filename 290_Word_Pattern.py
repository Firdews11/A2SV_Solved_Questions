class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        char_word = {}
        word_char = {}
        for char, word in zip(pattern, s):
            if char in char_word and char_word[char] != word:
                return False
            if word in word_char and word_char[word] != char:
                return False
            char_word[char] = word
            word_char[word] = char
        return True
