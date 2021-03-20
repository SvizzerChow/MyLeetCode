class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length < 1:
            return 0
        indexMap = {}
        for i in range(length):
            if s[i] not in indexMap:
                indexMap[s[i]] = []
            indexMap[s[i]].append(i)
        if len(indexMap) == 1:
            return (1+length)*length//2
        index = 0
        count = length
        while index < length-1:
            count += self._count(s, index, indexMap)
            index += 1
        return count

    def _count(self, s, index, indexMap):
        temp = indexMap[s[index]]
        tempIndex = len(temp) - 1
        count = 0
        while tempIndex > 0:
            end = temp[tempIndex]
            if end <= index:
                break
            mid = (end - index) // 2
            k = 1
            flag = True
            while k <= mid:
                if s[index+k] != s[end-k]:
                    flag = False
                    break
                k += 1
            if flag:
                count += 1
            tempIndex -= 1
        return count

print(Solution().countSubstrings("bbccaacac"))