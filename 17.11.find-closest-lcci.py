from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        if len(self.index) == 0:
            for i in range(len(words)):
                temp = self.index.get(words[i])
                if temp is None:
                    temp = []
                    self.index[words[i]] = temp
                temp.append(i)

        return self.getMin(self.index[word1], self.index[word2])

    def getMin(self, l1, l2):
        minValue = 100000
        for value in l1:
            low = 0
            hightValue = len(l2) - 1
            i = hightValue // 2
            while low < hightValue-1:
                if l2[i] < value:
                    low = i
                else:
                    hightValue = i
                i = (low + hightValue) // 2
            temp = abs(value - l2[low])
            if abs(value - l2[hightValue]) < temp:
                temp = abs(value - l2[hightValue])
            if minValue > temp:
                minValue = temp
        return minValue

    def __init__(self):
        self.index = {}

t = ["mm","l","tul","nd","up","ugu","sgn","bly","o","psn","dn","jw","uo","ry","z","kyb","en","a","aem","vcy","y","z","wuu","ver","l","wi","jh","nfu","quq","wa","zy","lyu","vny","v","k","p","k","buu","w","b","jl","mwv","v","til","mv","mv","m","uar","dbo","ae"]
w1 = "w"
w2 = "l"
print(Solution().findClosest(t, w1, w2))
