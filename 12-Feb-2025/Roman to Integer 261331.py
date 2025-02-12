# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        i = len(s) - 1
        n = len(s)
        num = 0
        while(i > -1):
            char = s[i]
            if i > 0 and roman_map[char] > roman_map[s[i - 1]]:
                num += roman_map[char] - roman_map[s[i - 1]]
                i -= 2
            else:
                num += roman_map[char]
                i -= 1
        return num