class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = []


        while i< len(word1) and i< len(word2):
            result.append(word1[i])
            result.append(word2[j])

            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[j:])


        return "".join(result)
