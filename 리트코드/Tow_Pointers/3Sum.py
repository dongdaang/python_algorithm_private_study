class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == s:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] > s:
                    r -= 1
                else:
                    l += 1
        return res
                    
a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))