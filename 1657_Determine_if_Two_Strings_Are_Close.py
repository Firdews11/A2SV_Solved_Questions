class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        hash1 = Counter(word1)
        hash2 = Counter(word2)

        if hash1.keys() != hash2.keys():
            return False

        if sorted(hash1.values()) != sorted(hash2.values()):
            return False
        return True
