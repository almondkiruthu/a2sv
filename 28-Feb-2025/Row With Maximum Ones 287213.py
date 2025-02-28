# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row_one_map = {}
        count = 0
        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            # track the current_one_count for each row.
            curr_one_row_count = 0
            for col in range(cols):
                val = mat[row][col]
                if val == 1:
                    curr_one_row_count += 1
            
            # for each row add the one frequency for each row
            if row not in row_one_map:
                row_one_map[row] = curr_one_row_count
            count = max(count, curr_one_row_count)

        row_index = float("inf")
        for key, value in row_one_map.items():
            # obtain the smallest row index if a row maps to the current max one count.
            if value == count:
                row_index = min(row_index, key)
        
        return [row_index, count]

        