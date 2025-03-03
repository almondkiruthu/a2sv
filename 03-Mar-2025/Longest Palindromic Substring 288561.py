# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_prime = "#" + "#".join(s) + "#"

        # the lenght of the prime string
        n = len(s_prime)

        # create a list P where we store the longest palindrome length
        p = [0] * n
        # the center of the previous palindrome that extends to the right the most
        # and is initially set to zero
        center = 0
        
        for i in range(n):
            # check if character is part of the previous palindrome
            if i < center + p[center]:
                # set the min between the rightmost character of a palindrome or
                # copy the value of the mirror i.e. i-prime
                p[i] = min(center + p[center] - i, p[2 * center - i])
            
            left, right = i - p[i] - 1, i + p[i] + 1

            while left > - 1 and right < n and s_prime[left] == s_prime[right]:
                p[i] += 1
                left -= 1
                right += 1
            # if the rightmost character of curr palindrome is greater than rightmost char of prev palindrome.
            if i + p[i] > center + p[center]:
                center = i
        
        # obtain the max palindrome length on both left and right sides.
        max_length = max(p)

        # index of center character
        max_index = p.index(max_length)

        start_index = (max_index - max_length) // 2

        return s[start_index:start_index + max_length]

