# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        
        def backtrack(i, cur, total):
            # successfull case
            if total == target:
                res.append(cur.copy())
                return
            # unsuccessful case
            if i >= len(candidates) or total > target:
                return

            # Left side use the number
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            #Right side don't use the numnber
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur, total)

        backtrack(0, cur, 0)
        return res

            
        