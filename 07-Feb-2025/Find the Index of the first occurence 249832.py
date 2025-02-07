# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # build the lookup table.
        table = [0 for _ in range(len(needle))]
        index = 0
        needle_pointer = 1
        while needle_pointer < len(needle):
            if needle[index] == needle[needle_pointer]:
                index += 1
                table[needle_pointer] = index
                needle_pointer += 1
            elif index > 0:
                index = table[index - 1]
            else:
                needle_pointer += 1

        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = table[j - 1]
            else:
                i += 1
        if j == len(needle):
            return i - j
        return -1