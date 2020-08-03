class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        temp = 0
        length1 = len(num1)
        length2 = len(num2)
        result = ''
        for i in range(length1):
            if i <= length2 - 1:
                temp += ord(num2[length2 - 1 - i]) - 48
            total = ord(num1[length1 - 1 - i]) - 48 + temp
            if total >= 10:
                temp = 1
                total -= 10
            else:
                temp = 0
            result = str(total) + result
        if length2 > length1:
            for j in range(length2 - length1 - 1, -1, -1):
                total = ord(num2[j]) - 48 + temp
                if total >= 10:
                    temp = 1
                    total -= 10
                else:
                    temp = 0
                result = str(total) + result
        if temp > 0:
            result = str(temp) + result
        return result


print(Solution().addStrings("9", "99"))