from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        if len(prices) < 2:
            return 0
        tempStart = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[tempStart]:
                temp = prices[i] - prices[tempStart]
                if temp > maxDiff:
                    maxDiff = temp
            if prices[i] < prices[tempStart]:
                tempStart = i
        return maxDiff if maxDiff > 0 else 0



print(Solution().maxProfit([2,7,1,4]))


