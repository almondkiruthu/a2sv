# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        res = 0
        for word in words:
            good_word_flag = True
            curr_word_count = {}
            for char in word:
                if char in curr_word_count:
                    curr_word_count[char] += 1
                else:
                    curr_word_count[char] = 1
                
                # compare our curr_word_map with char_count map

                # if char is not in chars map or count is greater than char count break and set
                # flag to false
                if char not in char_count or curr_word_count[char] > char_count[char]:
                    good_word_flag = False
                    break
            if good_word_flag == True:
                res += len(word)

        return res

