# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)

        start = 0 
        end = n - 1
        while start <= end:
            middle = start + (end - start) // 2
            if target < letters[middle]:
                end = middle - 1
            else:
                start = middle + 1
        
        return letters[start % n]
        