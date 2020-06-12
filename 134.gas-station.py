from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        beforeCost = 0
        r = 0
        for i in range(len(gas)):
            temp = gas[i] - cost[i]
            if total + temp >= 0:
                totalTemp = total + temp
                flag = False
                for j in range(i+1, len(gas)):
                    tp = gas[j] - cost[j]
                    if totalTemp + tp < 0:
                        flag = True
                        break
                    else:
                        totalTemp += tp
                if not flag:
                    if totalTemp + beforeCost >= 0:
                        return i
            if temp > 0:
                r += temp
            else:
                if r > 0:
                    temp = r + temp
                    if temp > 0:
                        r = temp
                        continue
                    else:
                        r = 0
                beforeCost += temp
        return -1


gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(Solution().canCompleteCircuit(gas, cost))


