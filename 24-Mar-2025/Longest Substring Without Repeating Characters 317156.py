# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_length = 0
        # remember the last index of each character that has been processed.
        char_index_map= {}

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_index_map:
                # if the right char has already been seen.
                # so there's no need to point the pointer to the current character we point to the next one
                # to shrink our window.
                window_start = max(window_start, char_index_map[right_char] + 1)
            char_index_map[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)

        return max_length