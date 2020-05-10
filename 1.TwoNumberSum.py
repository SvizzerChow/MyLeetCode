

class Solution: 
    def twoSum(self, nums, target):
        if len(nums) <=1:
            return []
        m = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in m:
                values = m[want]
                return [values, i]
            else:
                m[nums[i]] = i
        return []


s = Solution()

nums = [3,2,4]

print(s.twoSum(nums, 6))
    
