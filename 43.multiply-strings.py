class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result = [0] * (len(num1)+len(num2))
        index = 0
        for i in range(len(num1)-1, -1, -1):
            up = 0
            for j in range(len(num2)-1, -1, -1):
                temp = self.getNum(num1[i]) * self.getNum(num2[j]) + result[len(num1)+j-index] + up
                result[len(num1)+j-index] = temp % 10
                up = temp // 10
            if up > 0:
                self.add(result, up, len(num1) - index - 1)
            index += 1
        return self.display(result)

    def getNum(self, n):
        return ord(n)-ord('0')

    def add(self, result, data, i):
        while data > 0:
            temp = result[i] + data
            result[i] = temp % 10
            data = temp // 10
            i -= 1

    def display(self, result):
        s = ""
        for i in range(len(result)):
            if s == "" and result[i] == 0 and (i == 0 or result[i-1] == 0):
                continue
            s += str(result[i])
        return s




print(Solution().multiply("1", "4"))