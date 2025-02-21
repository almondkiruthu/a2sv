# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(set)
        for word in words:
            lookup[word] = set(word)

        def compare_words(s, t):
            if lookup[s] & lookup[t]:
                return False
            else:
                return True

        res = 0

        for s in words:
            for t in words:
                if compare_words(s, t):
                    res = max(res, len(s) * len(t))

        return res
        