# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_word_signature = set(allowed)
        for word in words:
            word_set = set(word)
            if word_set.issubset(allowed_word_signature):
                count += 1
        return count