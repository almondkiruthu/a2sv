# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])

        res = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                total = 0
                count = 0
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if i < 0 or i == rows or j < 0 or j == cols:
                            continue
                        total += img[i][j]
                        count += 1
                res[row][col] = total // count

        return res
