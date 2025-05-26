# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []  
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                print(curStr)
                res.append(curStr[::])
                return
            digit = digits[i]
            chars = phone[digit]
            for char in chars:
                backtrack(i + 1, curStr + char)
        if digits:
            backtrack(0, "")
        return res
        