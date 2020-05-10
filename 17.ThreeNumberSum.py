class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        numsMap = {}
        setList = []
        index = {}
        inc = 0
        for n in range(len(nums)):
            value = nums[n]
            x = numsMap.get(value)
            if x is None:
                setList.append(value)
                index[value] = inc
                inc = inc + 1
                numsMap[value] = x = set()
            x.add(n)
        result = []
        for iindex in range(inc):
            for jindex in range(iindex, inc):
                i = setList[iindex]
                if iindex == jindex and len(numsMap.get(i)) < 2:
                    continue
                j = setList[jindex]
                key = 0 - i - j
                x = numsMap.get(key)
                if x is None:
                    continue
                if index[key] < jindex:
                    continue
                length = len(x)
                if key == i and key == j and length < 3:
                    continue
                elif key == i and length < 2:
                    continue
                elif key == j and length < 2:
                    continue
                if length > 0:
                    result.append([i, j, key])
        return result
s = Solution()
print(s.threeSum([0,0,0]))
