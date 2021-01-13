class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        a = abs(dividend)
        b = abs(divisor)
        same = not (a == dividend) ^ (b == divisor)
        result = self.getNum(a, b)

        if result > (2**31 - 1) or result < -2**31:
            result = 2**31 - 1
        return result if same else -result

    def getNum(self, dividend, divisor):
        if dividend < divisor:
            return 0
        counter = 1
        p = divisor
        while p + p < dividend:
            p = p + p
            counter = counter + counter
        return counter + self.getNum(dividend - p, divisor)


print(Solution().divide(1, -1))