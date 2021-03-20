from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        counter = set()
        for i in nums:
            for j in list(counter):
                counter.add(j+i)
            counter.add(i)
            total += i
        if total % 2 > 0:
            return False
        half = total // 2
        return half in counter

print(Solution().canPartition([1,5,11,5]))