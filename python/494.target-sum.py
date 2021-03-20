from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        minValue = None
        total = 0
        numZero = 0
        for n in nums:
            total += n
            if minValue is None or n < minValue:
                minValue = n
            if n == 0:
                numZero += 1
        if numZero > 0:
            numZero = 2**numZero - 1
        x = abs(total - S)
        if x == 0:
            return 1 + numZero
        if S > total or x % 2 == 1:
            return 0
        x = x // 2
        if x < minValue:
            return 0
        return self._getSum(x, sorted(nums, reverse=True))

    def _getSum(self, count, nums):
        counter = [0] * (count + 1)
        for n in nums:
            if n > count:
                continue
            for j in range(count, n, -1):
                if counter[j - n] > 0:
                    counter[j] += counter[j - n]
            counter[n] += 1
        return counter[count]


nums= [9,7,0,3,9,8,6,5,7,6]
s = 2
print(Solution().findTargetSumWays(nums, s))