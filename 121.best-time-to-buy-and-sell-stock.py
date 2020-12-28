from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # [0, 0, 0]之前赚的的最大值，之前买入的最小，买入，卖出
        buys = [[0, 0, 0, 0] for _ in range(len(prices))]
        buys[0][1] = prices[0]
        buys[0][2] = prices[0]
        for i in range(1, len(prices)):
            buys[i][0] = max(buys[i-1][0], buys[i-1][-1])
            buys[i][1] = min(buys[i-1][1], buys[i-1][2])
            buys[i][2] = prices[i]
            buys[i][3] = prices[i] - buys[i][1]
        print(buys)
        return max(buys[-1][0], buys[-1][3])

print(Solution().maxProfit([7,1,5,3,6,4]))


