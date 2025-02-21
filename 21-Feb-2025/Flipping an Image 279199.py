# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for row in range(n):
            image[row].reverse()
        
        for row in range(n):
            for col in range(n):
                val = image[row][col]
                if val == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0

        return image

        