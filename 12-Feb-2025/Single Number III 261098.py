# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1_xor_n2 = 0
        for num in nums:
            n1_xor_n2 ^= num
        
        right_most_set_bit = 1
        while right_most_set_bit & n1_xor_n2 == 0:
            right_most_set_bit = right_most_set_bit << 1

        mask = right_most_set_bit

        # for every num find if bit is set
        first_unique_value = 0
        second_unique_value = 0
        for num in nums:
            if num & mask != 0:
                first_unique_value ^= num
            else:
                second_unique_value ^= num

        return [first_unique_value, second_unique_value]