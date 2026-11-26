class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(word):
            freq = {}

            for char in word:
                freq[char] = freq.get(char, 0) + 1

            return freq

        return count(s) == count(t)
