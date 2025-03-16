# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence_length = [1] * len(nums)
    
        i = 1
        for i in range(len(nums)):
            # reset j for every ith value
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    # pick the maximum value of the length of prev subsequence and current subsequence
                    # increment j
                    subsequence_length[i] = max(subsequence_length[i], subsequence_length[j] + 1)
                    j += 1
                else:
                    j += 1

        return max(subsequence_length)

        