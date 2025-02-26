# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1_one_positions = []
        img2_one_positions = []

        for row in range(n):
            for col in range(n):
                if img1[row][col] == 1:
                    img1_one_positions.append((row, col))
                if img2[row][col] == 1:
                    img2_one_positions.append((row, col))

        d = {}
        ans = 0
        for img1_x, img1_y in img1_one_positions:
            for img2_x, img2_y in img2_one_positions:
                translation = (img2_x - img1_x, img2_y - img1_y)
                if translation in d:
                    d[translation] += 1
                else:
                    d[translation] = 1
                ans = max(ans, d[translation])
        
        return ans
        