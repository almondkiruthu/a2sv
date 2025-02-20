# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:

        def find_square_num(num):
            total = 0
            while num > 0:
                digit = num % 10
                total = total + digit * digit
                num = num // 10
            return total

        
        slow, fast = n, n
        while True:
            slow = find_square_num(slow)
            fast = find_square_num(find_square_num(fast))

            if slow == fast:
                # found the cycle break
                break
        return slow == 1