from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counter = [float('inf')]*(amount+1)
        counter[0] = 0
        for coin in coins:
            for c in range(coin, amount+1):
                counter[c] = min(counter[c], counter[c - coin] + 1)
        return counter[amount] if counter[amount] < float('inf') else -1


coins = [1]
amount = 14
print(Solution().coinChange(coins, amount))


