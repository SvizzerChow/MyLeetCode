import collections
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ranges = [[] for _ in range(26)]
        for i in range(len(S)):
            temp = ranges[ord(S[i])-97]
            if len(temp) == 0:
                temp.append(i)
                temp.append(i)
            else:
                temp[1] = i
        result = {}
        for p in range(len(ranges)):
            temp = ranges[p]
            if len(temp) <= 0:
                continue
            start = temp[0]
            end = temp[1]
            for j in range(p+1, len(ranges)):
                tempJ = ranges[j]
                if len(tempJ) <= 0:
                    continue
                if tempJ[0] < start <= end < tempJ[1]:
                    start = tempJ[0]
                    end = tempJ[1]
                    ranges[j] = []
                elif start < tempJ[0] <= tempJ[1] < end:
                    ranges[j] = []
                elif start < tempJ[0] < end < tempJ[1]:
                    end = tempJ[1]
                    ranges[j] = []
                elif tempJ[0] < start < tempJ[1] < end:
                    start = tempJ[0]
                    ranges[j] = []
                elif start < tempJ[0] <= tempJ[1] < end:
                    ranges[j] = []
            result[start] = end - start + 1
        t = []
        for n in sorted(result.items(), key=lambda ele:ele[0]):
            t.append(n[1])
        return t

print(Solution().partitionLabels("caedbdedda"))




