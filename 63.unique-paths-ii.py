from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) < 1:
            return 0
        counter = [[0] * len(obstacleGrid[0])] * len(obstacleGrid)
        counter[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    counter[i][j] = 0
                    continue
                if i == j == 0:
                    continue
                total = 0
                if i - 1 >= 0:
                    total += counter[i-1][j]
                if j - 1 >= 0:
                    total += counter[i][j-1]
                counter[i][j] = total
        return counter[-1][-1]


obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(Solution().uniquePathsWithObstacles(obstacleGrid))

