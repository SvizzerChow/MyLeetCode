class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        if n < 10:
            return 1 if n >= 2 else 0
        strN = str(n)
        length = len(strN)
        count = self._counter(n, strN, 0, length)
        for j in range(length-1, 0, -1):
            count += self._counter(n, strN, j, length)
        return count

    def _counter(self, n, strN, start, end):
        count = 0
        length = len(strN)
        if strN[start] == '0':
            return 0
        num = int(strN[start:length])
        if num < 10:
            return 1 if num >= 2 else 0
        if end - start == 2:
            count = 1
        before = 1
        for i in range(start + 1, end):
            if i < length - 1:
                count = 10*before + 10 ** (i - start)
                before = count
            else:
                num = ord(strN[length - i - 1 + start]) - 48
                count = num * count
                if num >= 3:
                    count += 10 ** (i - start)
                elif num == 2:
                    count += int(strN[length - i + start:length]) + 1
        return count


print(Solution().numberOf2sInRange(559366752))


