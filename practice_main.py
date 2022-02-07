class Solution:
    def findMaxLength(self, nums):
        result = 0
        
        for i in range(2, len(nums)+1, 2):
            for j in range(len(nums)-i+1):
                if nums[j:i].count(0) == nums[j:i].count(1) and i > result:
                    result = i
        return result

a = Solution()
print(a.findMaxLength([0,0,1,0,0,0,1,1]))