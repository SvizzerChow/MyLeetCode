from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        k = len(prices) // 3 + 2
        income = [[[0, 0] for _ in range(k)] for _ in range(len(prices))]
        for m in range(k):
            income[0][m][1] = -prices[0]
        for i in range(1, len(prices)):
            income[i][0][1] = max(-prices[i], income[i-1][0][1])
        for j in range(1, len(prices)):
            for n in range(1, k):
                income[j][n][0] = max(income[j-1][n][0], income[j-1][n-1][1]+prices[j])
                income[j][n][1] = max(income[j-1][n][1], income[j-2][n][0] - prices[j])
        return income[-1][-1][0]


print(Solution().maxProfit([1,2,3,0,2]))
