class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


print(Solution().divisorGame(5))