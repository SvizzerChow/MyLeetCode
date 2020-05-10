class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows == 1:
            return s
        length = len(s)
        x = 2*numRows -2
        result = ""
        for row in range(numRows):
            for n in range(0, length, x):
                if n + row >= length:
                    break;
                result += s[n+row]
                t = 2*numRows - 2 + n - row
                if t >= length:
                    break
                if row != 0 and row != numRows-1:
                    result += s[t]
        return result

s = Solution()

print(s.convert("PAYPALISHIRING", 3))

