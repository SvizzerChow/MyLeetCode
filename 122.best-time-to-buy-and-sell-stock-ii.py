from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        total = 0
        start = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                total += prices[i-1] - prices[start]
                start = i
        return total if start == len(prices) - 1 else total + prices[len(prices)-1] - prices[start]


print(Solution().maxProfit([1, 3, 5, 7, 2, 6]))


