# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        numbers = sorted(nums)
        product_1 = numbers[-1] * numbers[-2] * numbers[-3]
        product_2 = numbers[0] * numbers[1] * numbers[-1]

        return max(product_1, product_2)


        