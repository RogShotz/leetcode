'''
2273. Find Resultant Array After Removing Anagrams
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
'''

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        # To find is something is an anagram you can either make a freq list or sort them.
        # If the sorted lists of both are the same then they are anagrams.
        def is_ana(s1, s2):
            return sorted(s1) == sorted(s2)
        
        result = []
        for word in words:
            if result and is_ana(result[-1], word): 
                continue
            result.append(word)

        return result