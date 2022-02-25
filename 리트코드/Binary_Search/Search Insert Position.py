class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)
    
a = Solution()
print(a.searchInsert([1,3,5,6], 5))