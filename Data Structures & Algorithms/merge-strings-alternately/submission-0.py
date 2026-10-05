class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        ni, mi = 0,0
        merged_word = []
        while (ni<n) and (mi<m):
            merged_word.append(word1[ni])
            merged_word.append(word2[mi])
            ni += 1
            mi += 1
        while ni<n:
            merged_word.append(word1[ni])
            ni += 1
        while mi<m:
            merged_word.append(word2[mi])
            mi += 1
        return "".join(merged_word)
        
        