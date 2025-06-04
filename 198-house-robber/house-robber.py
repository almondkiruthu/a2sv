class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        # we need to keep track of the cash of each path that we explore
        def explore(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            # option 1, : rob the current house and skip next
            rob_curr_house = nums[i] + explore(i + 2)
            # option 2, skip the current house
            skip_curr_house = explore(i + 1)
            cache[i] = max(rob_curr_house, skip_curr_house)
            return max(rob_curr_house, skip_curr_house)
        
        return explore(0)
        