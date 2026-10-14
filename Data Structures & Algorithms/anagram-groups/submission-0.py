
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}

        for word in strs:
            # sort word
            sorted_word = "".join(sorted(word))

            # create entry with no item in list first
            if sorted_word not in anagram_group:
                anagram_group[sorted_word] = []
            
            # add ori into the list
            anagram_group[sorted_word].append(word)

        return list(anagram_group.values())

