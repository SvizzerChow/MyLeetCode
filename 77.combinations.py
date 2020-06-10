from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = [1] * n
        result = []
        self._combine(temp, k, [], result)
        return result

    def _combine(self, temp, k, path, result):
        if k == 0:
            result.append(path)
            return path
        for i in range(len(temp)):
            if temp[i] == 0:
                continue
            temp[i] = 0
            self._combine(temp, k - 1, path + [i+1], result)
            temp[i] = 1
            if len(path) == 0:
                temp[i] = 0

        return result


print(Solution().combine(3, 2))




