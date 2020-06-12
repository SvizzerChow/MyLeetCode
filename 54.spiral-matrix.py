from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lengthH = len(matrix)
        if lengthH < 1:
            return []
        lengthW = len(matrix[0])
        h = w = 0
        result = []
        while h < lengthH / 2 and w < lengthW / 2:
            for temp in range(w, lengthW - w):
                result.append(matrix[h][temp])
            if h == lengthH - h - 1:
                break
            for temp in range(h + 1, lengthH - h):
                result.append(matrix[temp][lengthW - w - 1])
            if w == lengthW - w - 1:
                break
            for temp in range(lengthW - w - 2, w - 1, -1):
                result.append(matrix[lengthH - h - 1][temp])
            for temp in range(lengthH - h - 2, h, -1):
                result.append(matrix[temp][w])
            h += 1
            w += 1
        return result


matrix = [[2,5,8],[4,0,-1]]
print(Solution().spiralOrder(matrix))



