# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        m = len(matrix[0])

        def binary_search(arr, target=target):
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

        for row in range(rows):
            if binary_search(matrix[row]):
                return True

        return False
        