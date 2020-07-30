from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndex = {}
        for i in range(len(S)):
            lastIndex[S[i]] = i
        start = end = 0
        result = []
        for i in range(0, len(S)):
            s = S[i]
            if lastIndex[s] > end:
                end = lastIndex[s]
            if end == i:
                result.append(end - start + 1)
                start = end = i + 1
        return result

print(Solution().partitionLabels("caedbdedda"))
