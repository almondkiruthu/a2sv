# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        final_output = []
        current_line = []
        in_block_comment_flag = False

        for line in source:
            index, line_length = 0, len(line)

            while index < line_length:
                if in_block_comment_flag:
                    # check if in block comment ends on this line
                    if index + 1 < line_length and line[index:index + 2] == "*/":
                        in_block_comment_flag = False # end of block comment
                        index += 1 # skip the ending characters of the block comment
                else:
                    # check for the start of a block comment
                    if index + 1 < line_length and line[index:index + 2] == "/*":
                        in_block_comment_flag = True # start the block comment
                        index += 1 # skip the starting characters of the block comment
                    elif index + 1 < line_length and line[index:index + 2] == "//":
                        break # ignore the rest of the line no need to process it
                    else:
                        # add the current character to the line buffer
                        current_line.append(line[index]) 
                index += 1

            # if not in a block comment and the line buffer contatins chars add, to the result.
            if not in_block_comment_flag and current_line:
                final_output.append("".join(current_line))
                current_line.clear()
        
        return final_output