from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) < 1:
            return 0
        counter = [triangle[0]]
        for i in range(1, len(triangle)):
            n = []
            for j in range(len(triangle[i])):
                temp = None
                now = triangle[i][j]
                if 0 <= j - 1 < len(triangle[i - 1]):
                    temp = now + counter[i - 1][j-1]
                if j < len(triangle[i - 1]):
                    if temp is None or now + counter[i - 1][j] < temp:
                        temp = now + counter[i - 1][j]
                n.append(temp)
            counter.append(n)
        path = None
        for xx in counter[-1]:
            if path is None or path > xx:
                path = xx
        return path


t = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(t))
