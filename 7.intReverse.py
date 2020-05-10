class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        result = 0
        t = (2**31-1) /10
        t2 = 2**31 / 10
        q = x if x > 0 else -x
        while True:
            c = int(q % 10)
            if x>0 and (result > t or (result == t and c > 7)) :
                return 0
            if x<0 and result > t2:
                return 0
            result = result*10 + c
            q = int(q / 10)
            if q == 0:
                break
        return result if x > 0 else -result

s = Solution()

print(s.reverse(-123))
