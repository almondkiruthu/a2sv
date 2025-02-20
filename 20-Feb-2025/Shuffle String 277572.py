# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(s)

        for char, index in zip(s, indices):
            res[index] = char
        
        return "".join(res)
        