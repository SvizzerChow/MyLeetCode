from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False
        h = 0
        w = len(matrix[0]) - 1
        while h < len(matrix) and w >= 0:
            if matrix[h][w] == target:
                return True
            if matrix[h][w] > target:
                w -= 1
            else:
                h += 1
        return False
x = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
t =5
print(Solution().searchMatrix(x, t))