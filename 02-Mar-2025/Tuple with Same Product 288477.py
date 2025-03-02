# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product in d:
                    d[product] += 1
                else:
                    d[product] = 1
        count = 0
        for key in d:
            if d[key] > 1:
                # apply formula (k * k - 1) / 2 to find the possible n.o of combinations 
                # and multiply by 8 since they can be arranged in 8 different ways 
                count += (d[key] * (d[key] - 1)) // 2 * 8
        
        return count
       