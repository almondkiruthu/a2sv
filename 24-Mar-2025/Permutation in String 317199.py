# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        k = len(s1)
        s1_map = Counter(s1)
        s2_map = Counter()

        for window_end in range(len(s2)):
            right_char = s2[window_end]
            s2_map[right_char] += 1 # Add the new character to the window


            # shrink the window if it exceeds the lenght of the pattern
            if window_end >= k:
                left_char = s2[window_end - k]
                s2_map[left_char] -= 1
                if s2_map[left_char] == 0:
                    del s2_map[left_char]
            
            if s1_map == s2_map:
                return True

        return False
        