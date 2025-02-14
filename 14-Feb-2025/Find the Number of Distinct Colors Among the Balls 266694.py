# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_map = {}
        frequency_counter = Counter()
        res = []
        for i in range(len(queries)):
            query = queries[i]
            ball, colour = query
            # increase the counter for the colour Y
            frequency_counter[colour] += 1

            # if ball already exists in the map update the counter of the old colour 'Y' value
            if ball in ball_map:
                old_colour = ball_map[ball]
                frequency_counter[old_colour] -= 1
                
                # remove colour entry "Y" if the frequency becomes zero
                if frequency_counter[old_colour] == 0:
                    del frequency_counter[old_colour]
            
            # add the new ball and map it to it's new colour
            ball_map[ball] = colour
            res.append(len(frequency_counter)) 
        return res
        