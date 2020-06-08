from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        m = {}
        mMaxNum = {}
        maxLength = 0
        for i in range(len(nums)):
            temp = m.get(nums[i])
            if temp is None:
                temp = [i, i, 1]
                m[nums[i]] = temp
            else:
                temp[1] = i
                temp[2] = temp[2] + 1
            if temp[2] > maxLength:
                mMaxNum = {nums[i]: temp}
                maxLength = temp[2]
            elif temp[2] >= maxLength:
                mMaxNum[nums[i]] = temp
        if maxLength == 1:
            return 1
        minLength = 50001
        for key in mMaxNum.keys():
            t = mMaxNum[key][1] - mMaxNum[key][0] + 1
            if t < minLength:
                minLength = t
        return minLength


print(Solution().findShortestSubArray( [1,2,2,3,1]))