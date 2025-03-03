# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        d = {}
        word_list = s.split(" ")
        # find the longest word.
        max_length = max(len(word) for word in word_list)
        for word in word_list:
            for i in range(max_length):
                if i < len(word):
                    char = word[i]
                else:
                    char = " " # Add spaces for shorter words.
                if i in d:
                    d[i].append(char)
                else:
                    d[i] = [char]
        res = []
        for key in d:
            value = d[key]
            chars = "".join(value).rstrip()
            res.append(chars)
        return res