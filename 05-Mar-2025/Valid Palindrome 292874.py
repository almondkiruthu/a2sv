# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        build_up_string = []
        for char in s:
            if char.isalnum():
                build_up_string.append(char.lower()) # make sure to convert to lowercase.
        
        left = 0
        right = len(build_up_string) - 1

        while left <= right:
            if build_up_string[left] == build_up_string[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
        