class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 1. sort everything in alphabatically order
        groups = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

        