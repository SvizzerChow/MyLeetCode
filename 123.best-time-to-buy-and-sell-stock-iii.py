from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        result = 0
        temp = [0]
        x = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                if temp[-1] != x:
                    temp.append(x)
            else:
                x = i
        if temp[-1] != x:
            temp.append(x)
        if len(temp) == 1:
            result = prices[-1] - prices[0]
            return result if result > 0 else 0

        for i in range(1, len(temp)):
            one = self._getMax(prices, 0, temp[i]+1)
            two = self._getMax(prices, temp[i]+1, len(prices))
            if one + two > result:
                result = one + two
        return result

    def _getMax(self, prices, start, end):
        result = 0
        for i in range(start+1, end):
            if prices[i] < prices[start]:
                start = i
            elif prices[i] - prices[start] > result:
                result = prices[i] - prices[start]
        return result


data = [3, 2, 1]

print(Solution().maxProfit(data))
