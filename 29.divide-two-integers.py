class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        a = abs(dividend)
        b = abs(divisor)
        same = not (a == dividend) ^ (b == divisor)
        result = 0
        for i in range(32, -1, -1):
            if a - (b << i) >= 0:
                result += 2**i
                a -= (b << i)
        if result > (2**31 - 1) or result < -2**31:
            result = 2**31 - 1
        return result if same else -result


print(Solution().divide(-100, -100))