from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k == 1:
            return [[1]]
        result = []
        self._combine(0, n, k, [], result)
        return result

    def _combine(self, start, n, k, path, result):
        if k == 0:
            result.append(path)
            return
        for i in range(start, n):
            self._combine(i+1, n, k - 1, path + [i+1], result)


print(Solution().combine(4, 3))




