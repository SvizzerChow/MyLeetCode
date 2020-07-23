from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = None
                if j - 1 >= 0:
                    temp = grid[i][j-1]
                if i - 1 >= 0 and (temp is None or grid[i - 1][j] < temp):
                    temp = grid[i - 1][j]
                if temp is None:
                    temp = 0
                grid[i][j] += temp
        return grid[-1][-1]


print(Solution().minPathSum([[1,2],[1,1]]))