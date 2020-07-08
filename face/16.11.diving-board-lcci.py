from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        result = [shorter * k] * (k + 1)
        i = 1
        temp = longer - shorter
        x = result[0]
        while i <= k:
            x += temp
            result[i] = x
            i += 1
        return result


print(Solution().divingBoard(1, 2, 3))