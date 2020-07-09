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
        return self._getSum(x, nums, 0)

    def _getSum(self, count, nums, start):
        result = 0
        for i in range(start, len(nums)):
            if nums[i] > count:
                continue
            if nums[i] == count:
                result += 1
            result += self._getSum(count - nums[i], nums, i+1)
        return result


nums= [1,1,31,18,39,33,33,15,36,50,8,47,21,29,24,39,23,44,22,33]
s = 11
print(Solution().findTargetSumWays(nums, s))