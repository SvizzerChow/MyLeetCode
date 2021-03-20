from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buys = [[[0, 0] for _ in range(3)] for _ in range(len(prices))]
        buys[0][0][1] = -prices[0]
        buys[0][1][1] = -prices[0]
        for i in range(1, len(prices)):
            buys[i][0][0] = 0
            buys[i][0][1] = max(buys[i-1][0][1], -prices[i])

        for i in range(1, len(prices)):
            for k in range(1, 3):
                buys[i][k][0] = max(buys[i-1][k][0], buys[i-1][k-1][1] + prices[i])
                buys[i][k][1] = max(buys[i-1][k][1], buys[i-1][k][0] - prices[i])
        print(buys)
        return buys[-1][2][0]






data = [1, 2, 3, 1, 2]

print(Solution().maxProfit(data))
