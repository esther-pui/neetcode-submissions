class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        
        for s in strs:
            encode += str(len(s)) + '#' + s
        
        return encode

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            # read the length
            length = int(s[i:j])

            # extract ori string
            word = s[j + 1:j + 1 + length]
            result.append(word)

            # move to the beginning of the next encoded string
            i = j + 1 + length

        return result

