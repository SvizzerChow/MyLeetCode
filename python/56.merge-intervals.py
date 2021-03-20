from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0], reverse=False)
        result = []
        for i in range(len(intervals)):
            if len(result) == 0 or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result


intervals = [[1, 3], [2, 6], [8, 15], [15, 18]]
print(Solution().merge(intervals))