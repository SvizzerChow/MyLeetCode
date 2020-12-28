from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # [0, 0, 0]不交易，买入，卖出
        buys = [[0, 0, 0] for _ in range(len(prices))]
        buys[0][1] = -prices[0]
        for i in range(1, len(prices)):
            buys[i][0] = max(buys[i-1][0], buys[i-1][1], buys[i-1][2])
            buys[i][1] = -prices[i]
            t = buys[i-1][0]
            if t < 0:
                t = max(t, buys[i-1][1])
            else:
                t = buys[i-1][1]
            if t >= 0:
                continue
            buys[i][2] = prices[i] + t
        return max(buys[-1][0], buys[-1][2])



print(Solution().maxProfit([2,7,1,4]))


