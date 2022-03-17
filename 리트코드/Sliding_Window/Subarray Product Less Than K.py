class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        res = 0
        limit = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                res += i - limit
                continue
            else:
                tmp = 1
                for j in range(i, limit, -1):
                    tmp *= nums[j]
                    if tmp < k:
                        res += 1
                    else:
                        limit = j
                        break
        return res
                    
a = Solution()
print(a.numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19))