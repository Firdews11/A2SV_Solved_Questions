class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dic:
                anagram_dic[sorted_word].append(word)
            else:
                anagram_dic[sorted_word] = [word]        
        return list(anagram_dic.values())
