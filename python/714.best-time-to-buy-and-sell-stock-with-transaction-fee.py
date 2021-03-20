from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        if length < 2:
            return 0
        income = [[0, 0] for _ in range(length)]
        income[0][1] = -prices[0] - fee
        for i in range(1, length):
            income[i][0] = max(income[i-1][0], income[i-1][1] + prices[i])
            income[i][1] = max(income[i-1][1], income[i-1][0] - prices[i] - fee)
        return income[-1][0]

print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))

