# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = 0
        res = []
        for value in nums:
            if value % 2 == 0:
                sum_even += value
        
        for i in range(len(queries)):
            query = queries[i]
            value, index = query
            if nums[index] % 2 == 0:
                sum_even -= nums[index]

            nums[index] += value

            # check if number is even after operation if even add it back to the sum
            if nums[index] % 2 == 0:
                sum_even += nums[index]

            # add the current sum of even numbers to the res list
            res.append(sum_even)

        return res

        
        