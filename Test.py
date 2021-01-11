from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) <= 0:
            return -1
        counter = [0] * (amount+1)
        for coin in coins:
            if coin > amount:
                continue
            for i in range(coin, amount+1):
                if (i-coin == 0 or counter[i-coin] > 0) and (counter[i] == 0 or counter[i-coin] + 1 < counter[i]):
                    counter[i] = counter[i-coin] + 1
        return counter[amount] if counter[amount] > 0 else -1


print(Solution().coinChange([1, 2, 5], 11))