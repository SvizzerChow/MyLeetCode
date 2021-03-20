from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k <= 0:
            return 0
        if k > len(prices) // 2:
            k = len(prices) // 2
        k += 1
        buys = [[[0, 0] for _ in range(k)] for _ in range(len(prices))]
        for m in range(k):
            buys[0][m][1] = -prices[0]
        for n in range(1, len(prices)):
            buys[n][0][1] = max(-prices[n], buys[n-1][0][1])
        for i in range(1, len(prices)):
            for j in range(1, k):
                buys[i][j][0] = max(buys[i-1][j][0], buys[i-1][j-1][1] + prices[i])
                buys[i][j][1] = max(buys[i-1][j][1], buys[i-1][j][0] - prices[i])
        print(buys)
        return buys[-1][-1][0]


print(Solution().maxProfit(2, [1,2,3,4,2,5]))
