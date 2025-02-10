# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        n = len(s)

        # helper to find the palindrome for every char
        def find_palindromic_string(string, left, right):
            while left >= 0 and right < n and string[left] == string[right]:
                # longest palindrome seen so far is:
                left -= 1
                right += 1
            return string[left+1:right]

        for i in range(n):
            # Odd-length palindrome (single character center)
            odd_palindrome = find_palindromic_string(s, i, i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome

            # Even length palindrome (double character center)
            even_palindrome = find_palindromic_string(s, i, i+1)
            if len(even_palindrome) > len(res):
                res = even_palindrome
        
        return res