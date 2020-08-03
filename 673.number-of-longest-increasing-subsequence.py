from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        maxLength = 0
        counter = 0
        flags = [[0, 1] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                lengthJ = flags[i][0]
                if j < lengthJ - 1:
                    break
                if nums[j] < nums[i]:
                    length = flags[j][0]
                    c = flags[j][1]
                    if length + 1 < lengthJ:
                        continue
                    if length + 1 > lengthJ:
                        lengthJ = length + 1
                        flags[i][0] = lengthJ
                        flags[i][1] = 0
                    flags[i][1] += c
                    if flags[i][0] < maxLength:
                        continue
                    if flags[i][0] > maxLength:
                        maxLength = flags[i][0]
                        counter = 0
                    counter += c
        return counter if maxLength > 0 else len(nums)

print(Solution().findNumberOfLIS(
[1,3,5,4,7]))

