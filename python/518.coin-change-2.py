from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        counter = [0] * (amount + 1)
        if amount == 0:
            return 1
        for c in coins:
            if c > amount:
                continue
            counter[c] += 1
            for i in range(c+1, amount+1):
                counter[i] += counter[i - c]
        return counter[amount]


print(Solution().change(5, [1,2,5]))