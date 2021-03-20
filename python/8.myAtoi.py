class Solution:
    def myAtoi(self, str: str) -> int:
        f = None
        result = None
        for s in str:
            s = ord(s)
            if s == 45:
                if f is not None or result is not None:
                    break
                f = True
            elif s == 43:
                if f is not None or result is not None:
                    break
                f = False
            elif s >= 48 and s <= 57:
                if result is None:
                    result = s - 48
                else:
                    result = result*10 + s - 48
            elif s != 32 and result is None:
                break
            elif result is not None or f is not None:
                break
        if result is not None:
            if f and result > 2**31:
                result = 2**31
            elif not f and result > 2**31-1:
                result = 2**31-1
        if result is None:
            result = 0
        return result if not f else -result


s = Solution()


print(s.myAtoi("   -245  123"))
